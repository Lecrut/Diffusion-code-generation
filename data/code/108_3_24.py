import re

DATE_PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
DAY_INDEX = 2

def extract_day(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    match = DATE_PATTERN.match(date_str)
    if not match:
        raise ValueError(f"Invalid date format: {date_str}")
    return match.group(DAY_INDEX)

if __name__ == '__main__':
    sample_date = "2024-02-29"
    result = extract_day(sample_date)
    print(result)