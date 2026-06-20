MONTH_MAP = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}

def calculate_month_difference(month1_name, month2_name):
    if month1_name not in MONTH_MAP or month2_name not in MONTH_MAP:
        raise ValueError("Invalid month name provided.")
    return abs(MONTH_MAP[month1_name] - MONTH_MAP[month2_name])

if __name__ == '__main__':
    try:
        diff = calculate_month_difference("December", "March")
        print(diff)
        diff = calculate_month_difference("March", "November")
        print(diff)
        diff = calculate_month_difference("January", "March")
        print(diff)
    except ValueError as e:
        print(e)