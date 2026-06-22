from datetime import date, timedelta

def days_remaining_in_month():
    today = date.today()
    _, last_day_of_month = monthrange(today.year, today.month)
    return (date(today.year, today.month, last_day_of_month) - today).days

if __name__ == '__main__':
    print(days_remaining_in_month())