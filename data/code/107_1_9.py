from datetime import datetime

INPUT_FORMAT = '%m/%d/%Y'
OUTPUT_FORMAT = '%d-%m-%Y'

def transform_date(input_date: str) -> str:
    date_object = datetime.strptime(input_date, INPUT_FORMAT)
    return date_object.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    current_date = '01/01/2000'
    formatted = transform_date(current_date)
    print(formatted)