from datetime import date

def years_between_dates(start_date: date, end_date: date) -> int:
    year_diff = end_date.year - start_date.year
    month_day_diff = (end_date.month, end_date.day) < (start_date.month, start_date.day)
    return year_diff - month_day_diff

if __name__ == '__main__':
    start = date(2005, 11, 30)
    end = date(2023, 12, 31)
    print(years_between_dates(start, end))