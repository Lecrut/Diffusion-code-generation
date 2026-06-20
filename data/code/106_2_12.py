from datetime import datetime

def validate_dates(date1: datetime, date2: datetime) -> None:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be instances of datetime")
    if date1 > date2:
        raise ValueError("First date must be before the second date")

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    validate_dates(date1, date2)
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(2000, 5, 15)
    date2 = datetime(2023, 8, 20)
    difference = calculate_year_difference(date1, date2)
    print(difference)