import datetime

def days_remaining_in_month(year, month):
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    first_day_of_next_month = datetime.date(next_year, next_month, 1)
    last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
    return last_day_of_current_month.day
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))