from dateutil.parser import parse

DAY_OF_MONTH_KEY = "day"

def validate_date_string(input_text: str) -> str:
    if not isinstance(input_text, str):
        raise ValueError("Input must be a string")
    stripped = input_text.strip()
    if not stripped:
        raise ValueError("Input string cannot be empty")
    return stripped

def fetch_day_of_month(date_input: str) -> int:
    clean_input = validate_date_string(date_input)
    parsed_datetime = parse(clean_input)
    return parsed_datetime.day

if __name__ == '__main__':
    target_date = "2024-12-25"
    day_value = fetch_day_of_month(target_date)
    print(day_value)