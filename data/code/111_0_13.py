from datetime import date

def compute_year_day_count(start_date, end_date):
    if not isinstance(start_date, date):
        raise ValueError("start_date must be a date object")
    if not isinstance(end_date, date):
        raise ValueError("end_date must be a date object")
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    jan_first = date(2023, 1, 1)
    dec_last = date(2023, 12, 31)
    day_difference = compute_year_day_count(jan_first, dec_last)
    print(day_difference)