from datetime import datetime, timedelta

MONTH_DAYS = 30

def month_after(date):
    return date + timedelta(days=MONTH_DAYS)

if __name__ == '__main__':
    print(month_after(datetime(2023, 4, 15)))