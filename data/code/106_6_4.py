from datetime import datetime

def years_difference(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        return difference // 365
    except ValueError as e:
        print(f'Error parsing dates: {e}')
        return None

if __name__ == '__main__':
    sample_date1 = '2010-07-04'
    sample_date2 = '2022-12-25'
    result = years_difference(sample_date1, sample_date2)
    print(result)