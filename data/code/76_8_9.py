from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError as e:
        print(f'ValueError: {e}')
        return None

def calculate_days(date_str1, date_str2):
    if not (isinstance(date_str1, str) and isinstance(date_str2, str)):
        raise TypeError('Both inputs must be strings')

    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)

    if date1 is None or date2 is None:
        return None

    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    start_date = '2023-01-01'
    end_date = '2023-01-31'
    result = calculate_days(start_date, end_date)
    print(result)