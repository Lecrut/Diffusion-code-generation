from datetime import datetime

DATE_FORMAT = '%A, %B %d, %Y'

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime(DATE_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(format_date(sample_date))