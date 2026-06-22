from datetime import datetime

INPUT_FORMAT = "%Y-%m-%d"
OUTPUT_FORMAT = "%d/%m/%Y"

def validate_date_string(date_str: str) -> bool:
    if not isinstance(date_str, str):
        return False
    if len(date_str) != 10:
        return False
    if date_str[4] != '-' or date_str[7] != '-':
        return False
    return True

def convert_date_format(date_string: str) -> str:
    if not validate_date_string(date_string):
        raise ValueError("Invalid date string format")
    parsed_date = datetime.strptime(date_string, INPUT_FORMAT)
    return parsed_date.strftime(OUTPUT_FORMAT)

if __name__ == '__main__':
    sample_date = "2024-01-15"
    converted = convert_date_format(sample_date)
    print(converted)