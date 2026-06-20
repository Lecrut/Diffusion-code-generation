from datetime import datetime

def parse_date(date_str):
    return date_str.replace('-', '')

if __name__ == '__main__':
    sample_date = '25-Jan-2023'
    result = parse_date(sample_date)
    print(result)