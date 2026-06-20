from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%d-%b-%Y').strftime('%Y%m%d')

if __name__ == '__main__':
    sample_date = '15-Feb-2023'
    print(parse_date(sample_date))