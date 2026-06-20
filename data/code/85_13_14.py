from datetime import datetime

WEEKS_PER_DAY = 7

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs((date2 - date1).days)
        weeks = difference / WEEKS_PER_DAY
        return int(weeks)
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    print(calculate_week_difference('2023-01-15', '2023-02-28'))
    try:
        print(calculate_week_difference('2023-01-15', '01/15/2023'))
    except ValueError as e:
        print(e)