import datetime

def days_left_in_month(year, month):
    if month == 12:
        return 31 - (datetime.date(year, month, 1) - datetime.date(year, 1, 1)).days + 1
    else:
        next_month = (month % 12) + 1
        first_day_of_next_month = datetime.date(year, next_month, 1)
        last_day_of_current_month = first_day_of_next_month - datetime.timedelta(days=1)
        return last_day_of_current_month.day - (datetime.date(year, month, 1) - datetime.date(year, 1, 1)).days + 1

if __name__ == '__main__':
    print(days_left_in_month(2023, 10))