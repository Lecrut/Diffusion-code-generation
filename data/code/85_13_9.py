from datetime import datetime

WEEKS_PER_DAY = 7

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        weeks = difference / WEEKS_PER_DAY
        return round(weeks)
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    try:
        print(calculate_week_difference('2023-01-15', '2023-02-28'))
        print(calculate_week_difference('2023-02-28', '2023-01-15'))
        print(calculate_week_difference('2023-01-01', '2023-04-01'))
    except ValueError as e:
        print(e)