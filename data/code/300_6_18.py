from datetime import date, timedelta

def days_remaining_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    last_day_of_month = date(next_month[0], next_month[1], 1) - timedelta(days=1)
    today = date.today()
    return (last_day_of_month - today).days
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))