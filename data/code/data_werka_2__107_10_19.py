from datetime import datetime

DATE_INPUT_FORMAT = "%Y-%m-%d"
DATE_OUTPUT_FORMAT = "%d/%m/%Y"
SAMPLE_DATE_STRING = "2024-05-15"

def convert_date_format(date_string: str) -> str:
    try:
        parsed_date = datetime.strptime(date_string, DATE_INPUT_FORMAT)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}. Expected {DATE_INPUT_FORMAT}") from e
    return parsed_date.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_value = SAMPLE_DATE_STRING
    formatted_date = convert_date_format(sample_value)
    print(formatted_date)