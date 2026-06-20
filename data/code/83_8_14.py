import datetime

def are_same_day(date1: datetime.date, date2: datetime.date) -> bool:
    if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
        raise ValueError("Both inputs must be datetime.date objects")
    
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 26)
    d2 = datetime.date(2023, 10, 26)
    d3 = datetime.date(2023, 11, 1)
    d4 = datetime.date(2023, 10, 25)
    
    print(f"Is {d1} the same day as {d2}? {are_same_day(d1, d2)}")
    print(f"Is {d1} the same day as {d3}? {are_same_day(d1, d3)}")
    print(f"Is {d3} the same day as {d1}? {are_same_day(d3, d1)}")
    print(f"Is {d4} the same day as {d1}? {are_same_day(d4, d1)}")