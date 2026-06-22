from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def convert_date_format(date_str):
    return date_str.replace('/', '-')

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '01/01/2021', '07/4/2022']
    valid_dates = [date for date in sample_dates if validate_date_format(date)]
    formatted_dates = [convert_date_format(date) for date in valid_dates]
    print(formatted_dates)