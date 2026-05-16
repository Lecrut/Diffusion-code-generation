import datetime
def calculate_days_difference(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 == date2:
            return 0
        if date1 < date2:
            difference = date2 - date1
        else:
            difference = date1 - date2
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "2024-03-20"
    result = calculate_days_difference(date1, date2)
    print(result)