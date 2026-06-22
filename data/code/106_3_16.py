from datetime import date

def compute_year_gap(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Both arguments must be date objects")
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    years = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    d_start = date(2010, 5, 20)
    d_end = date(2023, 10, 15)
    gap = compute_year_gap(d_start, d_end)
    print(gap)