import re

def extract_day(date_string: str) -> int:
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_string)
    if not match:
        raise ValueError(f"Invalid date format: {date_string}")
    return int(match.group(3))

if __name__ == '__main__':
    result = extract_day("2023-10-05")
    print(result)