from datetime import datetime

SOURCE_FORMAT = '%d-%m-%Y %H:%M:%S'
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S'

def transform_date(input_date: str) -> str:
    parsed = datetime.strptime(input_date, SOURCE_FORMAT)
    return parsed.strftime(ISO_FORMAT)

if __name__ == '__main__':
    sample = '15-08-2023 09:15:30'
    converted = transform_date(sample)
    print(converted)