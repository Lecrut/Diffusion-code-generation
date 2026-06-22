import re

def convert_date(date_str: str) -> str:
    pattern = r'^(\d{2})/(\d{2})/(\d{4})$'
    match = re.match(pattern, date_str)
    if not match:
        raise ValueError("Date string must be in MM/DD/YYYY format")
    
    month_str, day_str, year_str = match.groups()
    
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if year < 1:
        raise ValueError("Year must be positive")
    
    return f"{year}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    sample_date = "05/20/2024"
    converted = convert_date(sample_date)
    print(converted)