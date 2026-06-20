from datetime import datetime

def parse_date(date_str):
    try:
        date_format = '%Y-%m-%d'
        return datetime.strptime(date_str, date_format)
    except ValueError:
        raise TypeError(f"Invalid date format: {date_str}")

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
    start_date = '2023-02-01'
    end_date = '2023-03-01'
    result = calculate_days(start_date, end_date)
    print(result)