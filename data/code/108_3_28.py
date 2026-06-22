import re

DATE_FORMAT_PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')
DAY_INDEX = 3
EXPECTED_PARTS = 3

def extract_day(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    
    match = DATE_FORMAT_PATTERN.match(date_str)
    if match:
        return match.group(DAY_INDEX)
    
    parts = date_str.split('-')
    if len(parts) != EXPECTED_PARTS:
        raise ValueError("Date string must have three parts")
    
    return parts[DAY_INDEX - 1]

if __name__ == '__main__':
    sample_date = "2024-05-15"
    result = extract_day(sample_date)
    print(result)