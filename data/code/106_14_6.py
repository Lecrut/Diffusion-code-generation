from datetime import datetime

def compute_year_span(start_date: datetime, end_date: datetime) -> int:
    year_start = start_date.year
    year_end = end_date.year
    month_start = start_date.month
    month_end = end_date.month
    day_start = start_date.day
    day_end = end_date.day
    is_full_year = (month_end > month_start) or (month_end == month_start and day_end >= day_start)
    raw_difference = year_end - year_start
    if raw_difference < 0:
        return abs(raw_difference)
    if is_full_year:
        return raw_difference
    return raw_difference - 1

if __name__ == '__main__':
    dt_a = datetime(2010, 12, 31)
    dt_b = datetime(2020, 1, 1)
    span = compute_year_span(dt_a, dt_b)
    print(span)