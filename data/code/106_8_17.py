from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime instance")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime instance")
    
    delta = relativedelta(end_date, start_date)
    return delta.years

if __name__ == '__main__':
    d1 = datetime(2020, 3, 15)
    d2 = datetime(2024, 3, 14)
    diff = calculate_year_difference(d1, d2)
    print(diff)