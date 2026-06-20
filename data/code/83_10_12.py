from datetime import datetime

def are_dates_identical(date1: datetime, date2: datetime) -> bool:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Inputs must be instances of datetime.")
    return date1.date() == date2.date()

if __name__ == '__main__':
    date_a = datetime(2023, 10, 26)
    date_b = datetime(2023, 10, 26)
    date_c = datetime(2023, 10, 27)
    print(f"Comparing {date_a} and {date_b}: {are_dates_identical(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {are_dates_identical(date_a, date_c)}")