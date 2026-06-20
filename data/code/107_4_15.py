from datetime import datetime

def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def transform_date(date_string):
    if not validate_date_format(date_string):
        raise ValueError("Invalid date format")
    return date_string.replace('.', '-')

if __name__ == '__main__':
    sample_dates = ['12.05.2023', '01.01.2020', '31.12.2022']
    for date in sample_dates:
        try:
            result = transform_date(date)
            print(result)
        except ValueError as e:
            print(e)