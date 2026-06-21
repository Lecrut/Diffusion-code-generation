from datetime import date

def compute_age_years(start: date, end: date) -> int:
    if start > end:
        start, end = end, start
    years: int = end.year - start.year
    if end.month < start.month:
        years -= 1
    elif end.month == start.month:
        if end.day < start.day:
            years -= 1
    return years

if __name__ == '__main__':
    d_start: date = date(1990, 6, 15)
    d_end: date = date(2023, 6, 14)
    age_years: int = compute_age_years(d_start, d_end)
    print(age_years)