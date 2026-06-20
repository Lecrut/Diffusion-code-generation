from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def calculate_years_difference(date_str1: str, date_str2: str) -> int:
    try:
        date1 = datetime.strptime(date_str1, DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DATE_FORMAT)
        difference = abs((date2 - date1).days)
        years = difference // 365
        return years
    except ValueError as e:
        print(f'Error parsing dates: {e}')
        return None
if __name__ == '__main__':
    sample_date1 = '2000-01-01'
    sample_date2 = '2023-04-10'
    result = calculate_years_difference(sample_date1, sample_date2)
    print(result)