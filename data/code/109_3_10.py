from datetime import date

def days_left_in_month():
    today = date.today()
    month_end = date(today.year, today.month, 1) + timedelta(days=32)
    return (month_end - today).days

if __name__ == '__main__':
    print(days_left_in_month())