import calendar
def calculate_month_difference(month1_name, month2_name):
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    if month1_name not in month_map or month2_name not in month_map:
        raise ValueError("Invalid month name provided.")
    month1 = month_map[month1_name]
    month2 = month_map[month2_name]
    difference = abs(month1 - month2)
    return difference
if __name__ == '__main__':
    month_a = "March"
    month_b = "November"
    try:
        result = calculate_month_difference(month_a, month_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")