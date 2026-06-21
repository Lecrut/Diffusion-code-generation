from datetime import date

def get_year_difference(start: date, end: date) -> int:
    delta_days = (end - start).days
    years_approx = delta_days // 365
    if years_approx > 0:
        test_date = date(start.year + years_approx, start.month, start.day)
        if test_date > end:
            years_approx -= 1
    elif years_approx < 0:
        test_date = date(start.year + years_approx, start.month, start.day)
        if test_date < end:
            years_approx += 1
    return years_approx

if __name__ == '__main__':
    begin = date(1990, 10, 10)
    finish = date(2024, 10, 9)
    diff = get_year_difference(begin, finish)
    print(diff)