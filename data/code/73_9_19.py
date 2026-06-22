from datetime import date

def compute_days_span(start_str: str, end_str: str) -> int:
    year_start, month_start, day_start = map(int, start_str.split('-'))
    year_end, month_end, day_end = map(int, end_str.split('-'))
    start_date = date(year_start, month_start, day_start)
    end_date = date(year_end, month_end, day_end)
    time_diff = end_date - start_date
    return time_diff.days

if __name__ == '__main__':
    first_date = '2024-01-01'
    second_date = '2024-12-31'
    span = compute_days_span(first_date, second_date)
    print(span)