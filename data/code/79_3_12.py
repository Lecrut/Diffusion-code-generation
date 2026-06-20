from datetime import datetime, timedelta

def month_after(date):
    return date + timedelta(days=31)

if __name__ == '__main__':
    today = datetime(2023, 9, 30)
    one_month_later = month_after(today)
    print(one_month_later)