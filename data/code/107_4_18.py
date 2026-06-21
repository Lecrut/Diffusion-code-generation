from datetime import datetime

INPUT_FORMAT = "%d.%m.%Y"
OUTPUT_FORMAT = "%Y-%m-%d"
SEPARATOR = "-"

def transform_date(date_string: str) -> str:
    parsed_date = datetime.strptime(date_string, INPUT_FORMAT)
    return parsed_date.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    print(transform_date("25.12.2023"))
    print(transform_date("01.01.2000"))
    print(transform_date("31.12.1999"))