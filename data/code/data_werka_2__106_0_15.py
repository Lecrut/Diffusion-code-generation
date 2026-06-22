from datetime import date, timedelta

def validate_date_inputs(d1: date, d2: date) -> tuple:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    if d1.year < 1 or d2.year < 1:
        raise ValueError("Years must be positive")
    return (d1, d2)

def calculate_year_difference(start_date: date, end_date: date) -> int:
    d1, d2 = validate_date_inputs(start_date, end_date)
    if d1 > d2:
        d1, d2 = d2, d1
    years = d2.year - d1.year
    anniversary = d1.replace(year=d2.year)
    if d2 < anniversary:
        years -= 1
    return years

if __name__ == '__main__':
    start = date(2000, 2, 29)
    end = date(2024, 2, 28)
    result = calculate_year_difference(start, end)
    print(result)