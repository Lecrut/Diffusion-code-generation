import datetime

def same_week(date_a: datetime.date, date_b: datetime.date) -> bool:
    if not isinstance(date_a, datetime.date):
        raise ValueError("date_a must be a date instance")
    if not isinstance(date_b, datetime.date):
        raise ValueError("date_b must be a date instance")
    
    iso_a = date_a.isocalendar()
    iso_b = date_b.isocalendar()
    
    return iso_a[0] == iso_b[0] and iso_a[1] == iso_b[1]

if __name__ == '__main__':
    ref_date = datetime.date(2023, 1, 1)
    in_week_date = datetime.date(2023, 1, 5)
    out_week_date = datetime.date(2023, 1, 8)
    
    result_1 = same_week(ref_date, in_week_date)
    result_2 = same_week(ref_date, out_week_date)
    
    print(result_1)
    print(result_2)