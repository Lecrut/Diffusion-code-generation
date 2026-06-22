from datetime import date

def absolute_difference_in_years(date1: date, date2: date) -> int:
    delta = date2 - date1
    days = abs(delta.days)
    years_approx = days // 365
    return years_approx

if __name__ == '__main__':
    d1 = date(2020, 1, 1)
    d2 = date(2023, 1, 1)
    result = absolute_difference_in_years(d1, d2)
    print(result)