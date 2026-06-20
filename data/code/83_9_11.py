from datetime import datetime

def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def are_same_day(date1: str, date2: str) -> bool:
    return parse_date(date1).date() == parse_date(date2).date()

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