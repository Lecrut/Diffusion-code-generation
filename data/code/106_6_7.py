from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def years_difference(date_str1: str, date_str2: str) -> int:
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError('Both dates must be in YYYY-MM-DD format')

    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = '2000-01-01'
    sample_date2 = '2023-04-10'
    result = years_difference(sample_date1, sample_date2)
    print(result)