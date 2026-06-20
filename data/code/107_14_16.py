from datetime import datetime

DATE_INPUT_FORMAT = '%d-%m-%Y %H:%M:%S'
DATE_OUTPUT_FORMAT = '%Y-%m-%dT%H:%M:%S'

def convert_to_iso(date_string):
    try:
        dt_object = datetime.strptime(date_string, DATE_INPUT_FORMAT)
        return dt_object.strftime(DATE_OUTPUT_FORMAT)
    except ValueError:
        return None

if __name__ == '__main__':
    sample_date = '31-12-2023 23:59:59'
    print(f"Input: {sample_date}, Converted: {convert_to_iso(sample_date)}")