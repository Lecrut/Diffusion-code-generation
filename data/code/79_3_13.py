from datetime import datetime, timedelta

def month_after(date):
    try:
        return date.replace(month=date.month + 1)
    except ValueError:
        return date.replace(year=date.year + 1, month=1)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(month_after(sample_date))