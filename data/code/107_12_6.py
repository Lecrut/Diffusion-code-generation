import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d-%b-%Y')
        return True
    except ValueError:
        return False

def parse_date(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format. Please use 'DD-Mon-YYYY'")
    return datetime.datetime.strptime(date_str, '%d-%b-%Y').strftime('%Y%m%d')

if __name__ == '__main__':
    sample_date = '25-Jan-2023'
    print(parse_date(sample_date))