from datetime import date, timedelta

def months_between_dates(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both inputs must be instances of date.')
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    if date2.day < date1.day:
        month_diff -= 1
        if month_diff < 0:
            year_diff -= 1
            month_diff += 12
    return year_diff * 12 + month_diff
if __name__ == '__main__':
    try:
        d1 = date(2022, 3, 15)
        d2 = date(2023, 7, 10)
        print(months_between_dates(d1, d2))
    except ValueError as e:
        print(e)