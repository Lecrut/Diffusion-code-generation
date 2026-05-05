import datetime
def calculate_days_between(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return None
if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "2024-03-20"
    result = calculate_days_between(date1, date2)
    if result is not None:
        print(result)
    else:
        print("Error: Invalid date format provided.")