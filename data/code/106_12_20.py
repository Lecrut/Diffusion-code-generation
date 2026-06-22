from datetime import date

def calculate_years_between(start_date: date, end_date: date) -> float:
    delta = end_date - start_date
    days = delta.days
    years = days / 365.2425
    return years

if __name__ == '__main__':
    d1 = date(2000, 1, 1)
    d2 = date(2023, 1, 1)
    result = calculate_years_between(d1, d2)
    print(result)