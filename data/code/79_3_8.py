from datetime import datetime, timedelta

def month_after(date):
    return date + timedelta(days=30)

if __name__ == '__main__':
    sample_date = datetime(2023, 11, 5)
    one_month_later = month_after(sample_date)
    print(one_month_later)