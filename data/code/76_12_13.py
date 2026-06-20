from datetime import datetime

def days_between_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return abs((date2 - date1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
if __name__ == '__main__':
    print(days_between_dates('2023-01-01', '2023-01-31'))