from datetime import date, timedelta

def days_left_in_month():
    today = date.today()
    _, last_day_of_current_month = calendar.monthrange(today.year, today.month)
    last_day = date(today.year, today.month, last_day_of_current_month)
    return (last_day - today).days

if __name__ == '__main__':
    result = days_left_in_month()
    print(result)