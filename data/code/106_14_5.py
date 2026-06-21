from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    year1 = date1.year
    year2 = date2.year
    return abs(year1 - year2)

if __name__ == '__main__':
    d1 = datetime(2020, 1, 1)
    d2 = datetime(2025, 12, 31)
    result = calculate_year_difference(d1, d2)
    print(result)