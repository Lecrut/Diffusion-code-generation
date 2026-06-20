from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f'Invalid date format: {date_str}')

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    return date1 == date2
if __name__ == '__main__':
    date_a = '2023-10-27'
    date_b = '2023-10-27'
    date_c = '2023-10-28'
    print(f'Comparing {date_a} and {date_b}: {compare_dates(date_a, date_b)}')
    print(f'Comparing {date_a} and {date_c}: {compare_dates(date_a, date_c)}')