from datetime import datetime

def transform_date(date_str):
    return date_str.replace('.', '-')

if __name__ == '__main__':
    test_dates = ['01.02.2023', '29.04.2020', '15.12.1999']
    for date in test_dates:
        print(transform_date(date))