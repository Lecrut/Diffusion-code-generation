import datetime
def calculate_days_between(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-05-20"
    result = calculate_days_between(date1_input, date2_input)
    print(result)