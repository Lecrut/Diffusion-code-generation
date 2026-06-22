from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> float:
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime instance")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime instance")

    days_in_year = 365.2425
    total_days = (end_date - start_date).days
    if total_days < 0:
        return -abs(total_days) / days_in_year
    return total_days / days_in_year

if __name__ == '__main__':
    d1 = datetime(2000, 1, 1)
    d2 = datetime(2023, 12, 31)
    diff = calculate_year_difference(d1, d2)
    print(diff)