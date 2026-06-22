from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    start, end = (date1, date2) if date1 <= date2 else (date2, date1)
    years = end.year - start.year
    current_anniversary = start.replace(year=start.year + years)
    if end < current_anniversary:
        years -= 1
    return years

if __name__ == '__main__':
    d1 = datetime(2000, 2, 29)
    d2 = datetime(2023, 2, 28)
    result = calculate_year_difference(d1, d2)
    print(result)