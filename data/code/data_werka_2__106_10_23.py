from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Inputs must be datetime objects")
    start = min(date1, date2)
    end = max(date1, date2)
    years = end.year - start.year
    if (end.month, end.day) < (start.month, start.day):
        years -= 1
    return abs(years)

if __name__ == '__main__':
    d1 = datetime(2000, 2, 29)
    d2 = datetime(2024, 2, 28)
    result = calculate_year_difference(d1, d2)
    print(result)