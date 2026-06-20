from datetime import date, timedelta

def next_month(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    try:
        return date(year, month, day)
    except ValueError:
        if month == 2 and day == 29:
            return date(year, month, 28)
        else:
            return date(year, month, 1)
if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(next_month(sample_date))