from datetime import date

def calculate_year_difference(start_date: date, end_date: date) -> int:
    delta = end_date - start_date
    days = delta.days
    years_approx = days // 365
    if years_approx < 0:
        return -calculate_year_difference(end_date, start_date)
    if years_approx == 0:
        return 0
    check_date = start_date.replace(year=start_date.year + years_approx)
    if check_date > end_date:
        return years_approx - 1
    return years_approx

if __name__ == '__main__':
    start = date(2000, 1, 1)
    end = date(2023, 10, 15)
    result = calculate_year_difference(start, end)
    print(result)