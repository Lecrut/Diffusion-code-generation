from datetime import datetime, timedelta

ONE_MONTH = timedelta(days=30)

def month_after(date):
    return date + ONE_MONTH

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(month_after(sample_date))