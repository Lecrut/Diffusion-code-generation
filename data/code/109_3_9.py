from datetime import date

def days_left_in_month():
    today = date.today()
    month_last_day = date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
    return (month_last_day - today).days + 1
if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(days_left_in_month())