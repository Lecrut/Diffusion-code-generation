from datetime import datetime

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        weeks = difference // 7
        return weeks
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    print(calculate_week_difference(date1_str, date2_str))