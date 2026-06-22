from datetime import date

def compute_year_diff(start_date: date, end_date: date) -> int:
    full_years = end_date.year - start_date.year
    start_anniversary = date(end_date.year, start_date.month, start_date.day)
    if end_date < start_anniversary:
        full_years -= 1
    return full_years

if __name__ == '__main__':
    d_start = date(1990, 12, 25)
    d_end = date(2023, 12, 24)
    diff = compute_year_diff(d_start, d_end)
    print(diff)