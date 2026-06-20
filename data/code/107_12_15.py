from datetime import datetime

def parse_date(date_str):
    return date_str.replace('-', '').replace(' ', '')

if __name__ == '__main__':
    sample_date = '05-Jan-2023'
    print(parse_date(sample_date))