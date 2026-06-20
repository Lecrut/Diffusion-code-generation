import re

DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'

def is_valid_date(date_str: str) -> bool:
    return bool(re.match(DATE_PATTERN, date_str))

def are_same_day(date1: str, date2: str) -> bool:
    if not (is_valid_date(date1) and is_valid_date(date2)):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    return date1 == date2

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-26"
    date_c = "2023-10-27"
    
    print(f"Date A: {date_a}")
    print(f"Date B: {date_b}")
    print(f"Date C: {date_c}")
    print(f"A and B are same day: {are_same_day(date_a, date_b)}")
    print(f"A and C are same day: {are_same_day(date_a, date_c)}")
    print(f"B and C are same day: {are_same_day(date_b, date_c)}")