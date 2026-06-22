import datetime
import calendar

def check_same_week(date_a: datetime.date, date_b: datetime.date) -> bool:
    if not isinstance(date_a, datetime.date):
        raise ValueError("date_a must be a datetime.date object")
    if not isinstance(date_b, datetime.date):
        raise ValueError("date_b must be a datetime.date object")
    
    def get_week_tuple(dt):
        iso_year, iso_week, iso_day = dt.isocalendar()
        return (iso_year, iso_week)
    
    week_a = get_week_tuple(date_a)
    week_b = get_week_tuple(date_b)
    
    return week_a == week_b

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 7)
    d3 = datetime.date(2023, 1, 8)
    d4 = datetime.date(2023, 12, 31)
    d5 = datetime.date(2024, 1, 1)
    
    print(check_same_week(d1, d2))
    print(check_same_week(d1, d3))
    print(check_same_week(d4, d5))