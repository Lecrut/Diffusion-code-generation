from datetime import date

def compute_year_span(d_start: date, d_end: date) -> int:
    if d_start.year == d_end.year:
        return 0
    if d_start.year > d_end.year:
        d_start, d_end = d_end, d_start
    return d_end.year - d_start.year

if __name__ == '__main__':
    d_a = date(1999, 12, 31)
    d_b = date(2001, 1, 1)
    span = compute_year_span(d_a, d_b)
    print(span)