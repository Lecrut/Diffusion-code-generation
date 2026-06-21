from datetime import date

def get_absolute_year_diff(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    if d1.year == d2.year:
        return 0
    earlier, later = (d1, d2) if d1 < d2 else (d2, d1)
    if (later.month, later.day) < (earlier.month, earlier.day):
        return later.year - earlier.year - 1
    return later.year - earlier.year

if __name__ == '__main__':
    start_date = date(2018, 5, 10)
    end_date = date(2022, 5, 10)
    diff_years = get_absolute_year_diff(start_date, end_date)
    print(diff_years)