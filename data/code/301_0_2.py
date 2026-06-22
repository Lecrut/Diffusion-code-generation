from datetime import datetime

def convert_date_format(date_str):
    return date_str.replace('-', '/')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = convert_date_format(sample_date)
    print(converted_date)