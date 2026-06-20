from datetime import datetime

def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def are_same_day(date1: str, date2: str) -> bool:
    if not (is_valid_date(date1) and is_valid_date(date2)):
        raise ValueError("Both inputs must be valid 'YYYY-MM-DD' formatted dates.")
    
    return datetime.strptime(date1, '%Y-%m-%d').date() == datetime.strptime(date2, '%Y-%m-%d').date()

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