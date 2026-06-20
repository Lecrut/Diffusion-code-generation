from datetime import date, timedelta

def get_next_month_date(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    while day > 0:
        try:
            return date(year, month, day)
        except ValueError:
            day -= 1
if __name__ == '__main__':
    sample_date = date(2023, 2, 28)
    print(get_next_month_date(sample_date))