from datetime import date

def compute_year_span(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date):
        raise TypeError("start_date must be a datetime.date instance")
    if not isinstance(end_date, date):
        raise TypeError("end_date must be a datetime.date instance")
    
    normalized_start = date(start_date.year, 1, 1)
    normalized_end = date(end_date.year, 1, 1)
    
    total_days = (normalized_end - normalized_start).days
    
    return total_days // 365

if __name__ == '__main__':
    base = date(2018, 3, 14)
    target = date(2024, 11, 5)
    span = compute_year_span(base, target)
    print(span)