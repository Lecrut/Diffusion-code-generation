from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def calculate_days(date_str1, date_str2):
    try:
        date1 = parse_date(date_str1)
        date2 = parse_date(date_str2)
        delta = abs((date2 - date1).days)
        return delta
    except TypeError as e:
        print(f'TypeError: {e}')
        return None

if __name__ == '__main__':
    result = calculate_days('2023-01-01', '2023-01-31')
    print(result)