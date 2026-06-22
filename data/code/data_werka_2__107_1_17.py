from datetime import datetime

INPUT_FORMAT = '%m/%d/%Y'
OUTPUT_FORMAT = '%d-%m-%Y'

def convert_date_format(date_string):
    date_obj = datetime.strptime(date_string, INPUT_FORMAT)
    return date_obj.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    original_date = '07/04/2024'
    converted_date = convert_date_format(original_date)
    print(converted_date)