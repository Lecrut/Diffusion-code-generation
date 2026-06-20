from datetime import date, timedelta

def next_month(start_date):
    year = start_date.year
    month = start_date.month
    day = start_date.day
    if month == 12:
        new_year = year + 1
        new_month = 1
    else:
        new_year = year
        new_month = month + 1
    try:
        return date(new_year, new_month, day)
    except ValueError:
        if month == 2 and day > 28:
            return date(new_year, new_month, 28)
        elif month in [4, 6, 9, 11] and day > 30:
            return date(new_year, new_month, 30)
        else:
            raise
if __name__ == '__main__':
    sample_date = date(2023, 11, 30)
    print(next_month(sample_date))