import datetime

def calculate_week_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date2 - date1)
        weeks = difference.days / 7.0
        return weeks
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    result = calculate_week_difference(date1, date2)
    print(result)