from datetime import date

def calculate_year_span(start: date, end: date) -> int:
    if start > end:
        return -calculate_year_span(end, start)
    full_years = end.year - start.year
    anniversary = date(end.year, start.month, start.day)
    if end < anniversary:
        full_years -= 1
    return full_years

if __name__ == '__main__':
    d_start = date(2019, 11, 30)
    d_end = date(2023, 12, 1)
    span = calculate_year_span(d_start, d_end)
    print(span)