from datetime import datetime

DATE_FORMAT_INPUT = '%Y-%m-%d'
DATE_FORMAT_OUTPUT = '%d/%m/%Y'

def format_date(date_str):
    date_obj = datetime.strptime(date_str, DATE_FORMAT_INPUT)
    return date_obj.strftime(DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatted_date = format_date(sample_date)
    print(formatted_date)