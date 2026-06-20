from datetime import datetime, timedelta

def nearest_saturday(date):
    days_until_saturday = (5 - date.weekday()) % 7
    return date + timedelta(days=days_until_saturday)

if __name__ == '__main__':
    sample_date = datetime(2023, 11, 1)
    print(nearest_saturday(sample_date))