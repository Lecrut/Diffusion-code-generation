import calendar
def calculate_month_difference(month1_name, month2_name):
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    if month1_name not in month_map or month2_name not in month_map:
        raise ValueError("Invalid month name provided.")
    month1 = month_map[month1_name]
    month2 = month_map[month2_name]
    difference = abs(month1 - month2)
    return difference
if __name__ == '__main__':
    month_a = "December"
    month_b = "March"
    try:
        diff = calculate_month_difference(month_a, month_b)
        print(diff)
    except ValueError as e:
        print(e)