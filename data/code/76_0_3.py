import datetime
def calculate_days_between(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        if date1 > date2:
            difference = abs(date1 - date2)
        else:
            difference = date2 - date1
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1_input = "2023-01-01"
    date2_input = "2023-01-31"
    result = calculate_days_between(date1_input, date2_input)
    print(result)