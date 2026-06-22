from datetime import date

def compute_year_diff(start: date, end: date) -> int:
    year_span = end.year - start.year
    birthday_this_year = date(end.year, start.month, start.day)
    if end < birthday_this_year:
        return year_span - 1
    return year_span

if __name__ == '__main__':
    initial = date(1990, 11, 2)
    final = date(2023, 11, 1)
    diff = compute_year_diff(initial, final)
    print(diff)