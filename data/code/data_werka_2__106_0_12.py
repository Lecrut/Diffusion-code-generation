from datetime import datetime

def compute_year_span(date_a: datetime, date_b: datetime) -> int:
    years_a = date_a.year
    years_b = date_b.year
    month_a = date_a.month
    month_b = date_b.month
    day_a = date_a.day
    day_b = date_b.day
    if years_a > years_b:
        years_a, years_b = years_b, years_a
        month_a, month_b = month_b, month_a
        day_a, day_b = day_b, day_a
    span = years_b - years_a
    if month_b < month_a:
        span -= 1
    elif month_b == month_a and day_b < day_a:
        span -= 1
    return span

if __name__ == '__main__':
    start_dt = datetime(2010, 6, 15)
    end_dt = datetime(2024, 3, 10)
    calculated_span = compute_year_span(start_dt, end_dt)
    print(calculated_span)