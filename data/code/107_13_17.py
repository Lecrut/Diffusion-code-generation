import datetime

INPUT_FORMAT = '%Y/%m/%d'
OUTPUT_FORMAT = '%B %d, %Y'

def convert_date_format(date_string: str) -> str:
    parsed_date = datetime.datetime.strptime(date_string, INPUT_FORMAT)
    formatted_date = parsed_date.strftime(OUTPUT_FORMAT)
    return formatted_date

if __name__ == '__main__':
    sample_date = '2024/12/25'
    converted = convert_date_format(sample_date)
    print(converted)