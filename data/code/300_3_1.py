from datetime import date, timedelta

def days_left_in_month():
    today = date.today()
    _, last_day = monthrange(today.year, today.month)
    last_day_of_month = date(today.year, today.month, last_day)
    return (last_day_of_month - today).days

if __name__ == '__main__':
    print(days_left_in_month())