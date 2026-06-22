import datetime

INPUT_FORMAT: str = '%Y/%m/%d'
OUTPUT_FORMAT: str = '%B %d, %Y'
SAMPLE_DATE: str = '2024/01/15'

def transform_date(raw_date: str) -> str:
    parsed_date: datetime.datetime = datetime.datetime.strptime(raw_date, INPUT_FORMAT)
    formatted_date: str = parsed_date.strftime(OUTPUT_FORMAT)
    return formatted_date

if __name__ == '__main__':
    output: str = transform_date(SAMPLE_DATE)
    print(output)