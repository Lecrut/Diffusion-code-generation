from datetime import datetime

DATE_INPUT_FORMAT = '%Y-%m-%d'
DATE_OUTPUT_FORMAT = '%d/%m/%Y'

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, DATE_INPUT_FORMAT)
    return date_obj.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-12-25'
    converted_date = convert_date_format(sample_date)
    print(converted_date)