from datetime import datetime

def format_date(date_str):
    return date_str.replace('-', '/')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatted_date = format_date(sample_date)
    print(formatted_date)