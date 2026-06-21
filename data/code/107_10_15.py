from datetime import datetime

DATE_INPUT_FORMAT = "%Y-%m-%d"
DATE_OUTPUT_FORMAT = "%d/%m/%Y"

def convert_date_format(date_string: str) -> str:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    try:
        date_obj = datetime.strptime(date_string, DATE_INPUT_FORMAT)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}") from e
    return date_obj.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = "2024-01-15"
    formatted_date = convert_date_format(sample_date)
    print(formatted_date)