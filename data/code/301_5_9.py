from datetime import datetime

DATE_FORMAT_INPUT = "%d/%m/%Y %I:%M %p"
DATE_FORMAT_OUTPUT = "%Y-%m-%dT%H:%M:00"

def convert_date_format(date_str):
    dt_object = datetime.strptime(date_str, DATE_FORMAT_INPUT)
    return dt_object.strftime(DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = "15/08/2023 04:30 PM"
    converted_date = convert_date_format(sample_date)
    print(converted_date)