from datetime import datetime

DATE_FORMAT_INPUT = '%Y-%m-%d'
DATE_FORMAT_OUTPUT = '%d/%m/%Y'

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, DATE_FORMAT_INPUT)
    return date_obj.strftime(DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = convert_date_format(sample_date)
    print(converted_date)