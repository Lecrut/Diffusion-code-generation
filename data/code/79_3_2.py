from datetime import datetime, timedelta

def month_after(date):
    return date + timedelta(days=30)

if __name__ == '__main__':
    print(month_after(datetime(2023, 4, 15)))