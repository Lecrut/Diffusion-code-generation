from datetime import datetime

INPUT_FORMAT = '%d-%m-%Y %H:%M:%S'
OUTPUT_FORMAT = '%Y-%m-%dT%H:%M:%S'

def format_date(input_date: str) -> str:
    parsed_date = datetime.strptime(input_date, INPUT_FORMAT)
    return parsed_date.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = '01-01-2024 12:00:00'
    formatted = format_date(sample_date)
    print(formatted)