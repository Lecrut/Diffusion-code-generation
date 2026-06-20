from datetime import datetime

def transform_date(date_str):
    return date_str.replace('.', '-')
if __name__ == '__main__':
    print(transform_date('31.12.2020'))
    print(transform_date('01.01.2021'))