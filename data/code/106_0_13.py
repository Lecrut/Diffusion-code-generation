import datetime

def calculate_year_difference(date1: datetime.date, date2: datetime.date) -> int:
    delta = date2 - date1
    days = delta.days
    years_approx = days // 365
    if days < 0:
        years_approx = -(-days // 365)
        if (-years_approx * 365) < abs(days):
            years_approx -= 1
    else:
        if (years_approx * 365) > days:
            years_approx -= 1
    return years_approx

if __name__ == '__main__':
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2023, 1, 1)
    result = calculate_year_difference(start_date, end_date)
    print(result)