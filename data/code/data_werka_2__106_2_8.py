from datetime import datetime

def calculate_year_span(initial: datetime, final: datetime) -> int:
    if not isinstance(initial, datetime) or not isinstance(final, datetime):
        raise ValueError("Arguments must be datetime instances")
    if final < initial:
        raise ValueError("Final date must be on or after initial date")
    raw_span = final.year - initial.year
    current_anniversary = initial.replace(year=final.year)
    if final < current_anniversary:
        adjusted_span = raw_span - 1
    else:
        adjusted_span = raw_span
    return adjusted_span

if __name__ == '__main__':
    begin = datetime(1985, 11, 20)
    finish = datetime(2023, 11, 19)
    span_value = calculate_year_span(begin, finish)
    print(span_value)