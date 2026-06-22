from datetime import datetime

DATE_INPUT_FORMAT = "%Y-%m-%d"
DATE_OUTPUT_FORMAT = "%d/%m/%Y"
SAMPLE_DATE = "2024-01-15"

def convert_date_format(date_string: str) -> str:
    try:
        date_obj = datetime.strptime(date_string, DATE_INPUT_FORMAT)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")
    return date_obj.strftime(DATE_OUTPUT_FORMAT)

if __name__ == '__main__':
    print(convert_date_format(SAMPLE_DATE))