import datetime
def calculate_days(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        return abs((date2 - date1).days)
    except ValueError:
        return None
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2024-03-20"
    result = calculate_days(date1_str, date2_str)
    if result is not None:
        print(result)
    else:
        print("Error: Invalid date format provided.")