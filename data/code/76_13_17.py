from datetime import datetime

def get_date_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 10)
    difference1 = get_date_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference1} days")
    
    date_c = datetime(2024, 12, 31)
    date_d = datetime(2025, 1, 1)
    difference2 = get_date_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {difference2} days")