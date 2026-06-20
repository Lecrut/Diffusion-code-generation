from datetime import datetime, timedelta

def next_15th_day_of_month(date):
    year = date.year
    month = date.month + 1 if date.day >= 15 else date.month
    day = 15
    try:
        return datetime(year, month, day)
    except ValueError:
        return datetime(year + (month // 12), (month % 12) + 1, day)

if __name__ == '__main__':
    sample_date = datetime(2023, 3, 3)
    next_date = next_15th_day_of_month(sample_date)
    print(next_date)