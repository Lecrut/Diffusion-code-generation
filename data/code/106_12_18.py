from datetime import date

def calculate_years_between(date1: date, date2: date) -> int:
    delta = abs(date2 - date1)
    years = delta.days // 365
    days_in_partial_year = delta.days % 365
    if days_in_partial_year >= 180:
        years += 1
    return years

if __name__ == '__main__':
    d1 = date(2015, 7, 4)
    d2 = date(2030, 11, 21)
    print(calculate_years_between(d1, d2))