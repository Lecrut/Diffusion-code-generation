import datetime

def calculate_date_difference(date1: datetime.datetime, date2: datetime.datetime) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 15)
    date_b = datetime.datetime(2023, 3, 20)
    print(f"Difference between {date_a} and {date_b}: {calculate_date_difference(date_a, date_b)} days")
    
    date_c = datetime.datetime(2022, 12, 31)
    date_d = datetime.datetime(2023, 1, 1)
    print(f"Difference between {date_c} and {date_d}: {calculate_date_difference(date_c, date_d)} days")