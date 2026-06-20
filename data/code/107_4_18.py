from datetime import datetime

def transform_date(date_str):
    return datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
if __name__ == '__main__':
    print(transform_date('15.08.2023'))
    print(transform_date('01.01.2020'))
    print(transform_date('31.12.2021'))