import datetime

def get_next_month_date(start_date):
    year = start_date.year + (start_date.month // 12)
    month = (start_date.month % 12) + 1
    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
    day = min(start_date.day, days_in_month)
    return datetime.date(year, month, day)

if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 15)
    next_month_date = get_next_month_date(start_date)
    print(next_month_date.strftime('%Y-%m-%d'))