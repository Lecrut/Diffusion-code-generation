from datetime import datetime

def parse_date(date_str):
    try:
        date_format = '%Y-%m-%d'
        return datetime.strptime(date_str, date_format)
    except ValueError as e:
        print(f'ValueError: {e}')
        return None

def calculate_days(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    if date1 is not None and date2 is not None:
        delta = abs((date2 - date1).days)
        return delta
    else:
        return None

if __name__ == '__main__':
    result = calculate_days('2023-01-01', '2023-01-31')
    print(result)