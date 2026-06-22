from datetime import datetime

def convert_date_format(date_str):
    return date_str.replace('-', '/')

if __name__ == '__main__':
    sample_date = '2023-04-30'
    print(convert_date_format(sample_date))