from datetime import datetime

def get_year_span(start_date: datetime, end_date: datetime) -> int:
    delta_years = end_date.year - start_date.year
    month_day_adjustment = (end_date.month, end_date.day) < (start_date.month, start_date.day)
    return delta_years - (1 if month_day_adjustment else 0)

if __name__ == '__main__':
    start = datetime(1995, 12, 31)
    end = datetime(2024, 1, 1)
    span = get_year_span(start, end)
    print(span)