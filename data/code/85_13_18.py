from datetime import datetime

WEEKS_IN_YEAR = 52

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = abs((date2 - date1).days)
        weeks = (delta / WEEKS_IN_YEAR) * 52
        return int(weeks)
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    print(calculate_week_difference(date1_str, date2_str))