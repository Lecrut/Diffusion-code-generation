from datetime import date, timedelta

def get_next_month_date(current_date):
    year = current_date.year
    month = current_date.month
    day = current_date.day
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    while day > 0:
        try:
            date(year, month, day)
            break
        except ValueError:
            day -= 1
    return date(year, month, day)
if __name__ == '__main__':
    sample_date = date(2023, 11, 30)
    print(get_next_month_date(sample_date))