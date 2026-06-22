from datetime import date

DATE_UNITS = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365
}

def calculate_date_span(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Arguments must be date instances")
    delta = second - first
    return delta.days

if __name__ == '__main__':
    reference_dates = {
        "start": date(2021, 1, 1),
        "end": date(2021, 1, 15)
    }
    s = reference_dates["start"]
    e = reference_dates["end"]
    span = calculate_date_span(s, e)
    print(span)