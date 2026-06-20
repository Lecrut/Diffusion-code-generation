from datetime import datetime, timedelta

def get_next_month_date(date):
    if date.month == 12:
        return datetime(date.year + 1, 1, 1)
    else:
        return datetime(date.year, date.month + 1, 1)

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(get_next_month_date(sample_date))