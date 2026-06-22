import datetime

DATE_FORMAT_INPUT = '%Y-%m-%d'
DATE_FORMAT_OUTPUT = '%d %B %Y'

def convert_date_format(date_str: str) -> str:
    dt_object = datetime.datetime.strptime(date_str, DATE_FORMAT_INPUT)
    return dt_object.strftime(DATE_FORMAT_OUTPUT)

if __name__ == '__main__':
    sample_date = '2021-01-01'
    formatted_date = convert_date_format(sample_date)
    print(formatted_date)