import datetime

def same_week(date1: datetime.date, date2: datetime.date) -> bool:
    if not isinstance(date1, datetime.date):
        raise ValueError("date1 must be a date instance")
    if not isinstance(date2, datetime.date):
        raise ValueError("date2 must be a date instance")
    
    iso1 = date1.isocalendar()
    iso2 = date2.isocalendar()
    
    return iso1[0] == iso2[0] and iso1[1] == iso2[1]

if __name__ == '__main__':
    d_start = datetime.date(2024, 1, 1)
    d_mid = datetime.date(2024, 1, 5)
    d_next = datetime.date(2024, 1, 8)
    d_prev = datetime.date(2023, 12, 31)
    
    result1 = same_week(d_start, d_mid)
    result2 = same_week(d_start, d_next)
    result3 = same_week(d_start, d_prev)
    
    print(result1)
    print(result2)
    print(result3)