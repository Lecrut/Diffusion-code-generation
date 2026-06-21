import re

def extract_day_component(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    pattern = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
    match = pattern.search(date_str)
    if not match:
        raise ValueError("Date string does not match YYYY-MM-DD format")
    return match.group(3)

if __name__ == '__main__':
    test_date = "1999-01-01"
    day_part = extract_day_component(test_date)
    print(day_part)