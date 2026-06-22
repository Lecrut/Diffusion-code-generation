from datetime import datetime

DATE_INPUT_FORMAT = "%Y-%m-%d"
DATE_OUTPUT_FORMAT = "%d/%m/%Y"
SAMPLE_DATE = "2024-01-15"

def validate_date_format(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, DATE_INPUT_FORMAT)
        return True
    except ValueError:
        return False

def convert_date_format(date_string: str) -> str:
    if not validate_date_format(date_string):
        raise ValueError(f"Invalid date format: {date_string}")
    parsed_date = datetime.strptime(date_string, DATE_INPUT_FORMAT)
    return parsed_date.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    result = convert_date_format(SAMPLE_DATE)
    print(result)