from datetime import date

def calculate_year_difference(date1: date, date2: date) -> int:
    delta = date2 - date1
    days = delta.days
    years_approx = days // 365
    if years_approx < 0:
        return -calculate_year_difference(date2, date1)
    return years_approx

if __name__ == '__main__':
    d1 = date(2000, 1, 1)
    d2 = date(2023, 10, 15)
    result = calculate_year_difference(d1, d2)
    print(result)