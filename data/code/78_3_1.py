import calendar
def calculate_month_difference(month1_str, month2_str):
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    try:
        month1 = month_map[month1_str.lower()]
        month2 = month_map[month2_str.lower()]
        if month1 == month2:
            return 0
        elif month1 < month2:
            return month2 - month1
        else:
            return month1 - month2
    except KeyError:
        return "Invalid month name provided"
if __name__ == '__main__':
    month1 = "January"
    month2 = "March"
    difference = calculate_month_difference(month1, month2)
    print(difference)