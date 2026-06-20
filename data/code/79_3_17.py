from datetime import datetime, timedelta

def month_after(date):
    return (date.replace(day=28) + timedelta(days=4)).replace(day=1)

if __name__ == '__main__':
    print(month_after(datetime(2023, 10, 15)))