import re

DATE_FORMAT_MAP = {
    "YYYY-MM-DD": r"^(\d{4})-(\d{2})-(\d{2})$"
}

def extract_day(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    
    pattern_str = DATE_FORMAT_MAP.get("YYYY-MM-DD")
    if not pattern_str:
        raise ValueError("Unsupported date format")
        
    pattern = re.compile(pattern_str)
    match = pattern.match(date_str)
    
    if not match:
        raise ValueError(f"Invalid date format: {date_str}")
        
    return match.group(3)

if __name__ == '__main__':
    sample_date = "2023-10-05"
    day_value = extract_day(sample_date)
    print(day_value)