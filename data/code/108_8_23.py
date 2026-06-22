from dateutil.parser import parse

def get_day_from_date(date_string: str) -> int:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if not date_string.strip():
        raise ValueError("Input string cannot be empty")
    parsed_date = parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = "December 25, 2024"
    day_value = get_day_from_date(sample_date)
    print(day_value)