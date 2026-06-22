from datetime import datetime
INPUT_FORMAT = '%m/%d/%Y'
OUTPUT_FORMAT = '%d-%m-%Y'

def transform_date(date_str):
    dt_obj = datetime.strptime(date_str, INPUT_FORMAT)
    return dt_obj.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    raw_date = '07/04/2024'
    converted = transform_date(raw_date)
    print(converted)