from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    date1 = datetime(2020, 1, 1)
    date2 = datetime(2023, 4, 1)
    print(calculate_year_difference(date1, date2))