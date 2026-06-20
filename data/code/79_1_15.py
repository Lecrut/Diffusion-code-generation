from datetime import date, timedelta

def get_next_month_date(input_date):
    year = input_date.year
    month = input_date.month
    day = input_date.day
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    if month == 12:
        last_day_of_current_month = date(year, month, 31)
    elif month in [4, 6, 9, 11]:
        last_day_of_current_month = date(year, month, 30)
    else:
        last_day_of_current_month = date(year, month + 1, 1) - timedelta(days=1)
    if day > last_day_of_current_month.day:
        return date(next_year, next_month, 1)
    else:
        return input_date.replace(month=next_month)
if __name__ == '__main__':
    sample_date = date(2023, 4, 30)
    print(get_next_month_date(sample_date))