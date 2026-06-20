from datetime import datetime

def validate_dates(date1, date2):
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError('Both inputs must be instances of datetime')
    if date1 > date2:
        date1, date2 = (date2, date1)
    return (date1, date2)

def calculate_date_difference(date1, date2):
    delta = (date2 - date1).days
    years = delta // 365
    months = delta % 365 // 30
    days = delta % 365 % 30
    return f'{years} years, {months} months, and {days} days'

def date_difference(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    date1, date2 = validate_dates(date1, date2)
    return calculate_date_difference(date1, date2)
if __name__ == '__main__':
    result1 = date_difference('2023-01-01', '2023-01-10')
    print(f'Difference between 2023-01-01 and 2023-01-10: {result1}')
    result2 = date_difference('2024-05-15', '2024-04-01')
    print(f'Difference between 2024-05-15 and 2024-04-01: {result2}')
    result3 = date_difference('2022-12-31', '2023-01-01')
    print(f'Difference between 2022-12-31 and 2023-01-01: {result3}')