from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(2020, 2, 29)
    date2 = datetime(2023, 2, 28)
    print(calculate_year_difference(date1, date2))