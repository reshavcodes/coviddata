import requests
from bs4 import BeautifulSoup


def main_function(n):
    url = "https://www.mygov.in/corona-data/covid19-statewise-status"
    parsed_html = requests.get(url)

    soup = BeautifulSoup(parsed_html.content, "lxml")

    data = soup.find_all("div", class_="field-collection-view clearfix view-mode-full")
    main = {}
    for d in data:
        s = d.find("div",class_="field field-name-field-total-confirmed-indians field-type-number-integer field-label-above")
        s1 = s.find("div", class_="field-items").text
        main[d.find("div", class_="field-items").div.text] = s1
    return main[n]


if __name__ == "__main__":
    a = input("Enter the name of the state of which you want to see total confirmed corona cases of: ")

    final_data = main_function(a)
    
    # For printing the cases based on state key
    print("\n", final_data)  