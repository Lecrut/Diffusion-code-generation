import datetime
def calculate_days(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        return abs((date2 - date1).days)
    except ValueError:
        return None
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2024-03-20"
    days_difference = calculate_days(date1_input, date2_input)
    if days_difference is not None:
        print(days_difference)
    else:
        print("Error: Invalid date format provided.")