from datetime import datetime

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f'Invalid date format. Expected YYYY-MM-DD. Error: {e}')
    year_diff = date2.year - date1.year
    if (date2.month, date2.day) < (date1.month, date1.day):
        year_diff -= 1
    return abs(year_diff)
if __name__ == '__main__':
    start_date = '2010-05-15'
    end_date = '2023-05-14'
    result = compute_year_difference(start_date, end_date)
    print(result)