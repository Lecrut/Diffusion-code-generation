from datetime import date

YEARS_PER_CENTURY = 100
SAMPLE_START_YEAR = 1995
SAMPLE_END_YEAR = 2023
SAMPLE_START_MONTH = 3
SAMPLE_END_MONTH = 11
SAMPLE_DAY = 15

def compute_year_span(start_date: date, end_date: date) -> int:
    year_diff = end_date.year - start_date.year
    if end_date.month < start_date.month:
        year_diff -= 1
    elif end_date.month == start_date.month:
        if end_date.day < start_date.day:
            year_diff -= 1
    return year_diff

if __name__ == '__main__':
    start_dt = date(SAMPLE_START_YEAR, SAMPLE_START_MONTH, SAMPLE_DAY)
    end_dt = date(SAMPLE_END_YEAR, SAMPLE_END_MONTH, SAMPLE_DAY)
    span = compute_year_span(start_dt, end_dt)
    print(span)