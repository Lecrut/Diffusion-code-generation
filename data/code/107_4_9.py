from datetime import datetime

def transform_date(date_str):
    return date_str.replace('.', '-')

if __name__ == '__main__':
    test_dates = ['01.02.2023', '15.10.2022', '31.12.2021']
    for date in test_dates:
        print(transform_date(date))