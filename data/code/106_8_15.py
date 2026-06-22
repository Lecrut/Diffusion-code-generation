from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 15)
    dt2 = datetime(2025, 5, 20)
    result = calculate_year_difference(dt1, dt2)
    print(result)