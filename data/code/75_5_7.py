import datetime

def calculate_date_difference(date1: datetime.date, date2: datetime.date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = datetime.date(2023, 4, 1)
    date_b = datetime.date(2023, 5, 15)
    print(calculate_date_difference(date_a, date_b))