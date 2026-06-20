from datetime import datetime, timedelta

def add_year_and_day(date):
    return date + timedelta(days=365) + timedelta(days=1)

if __name__ == '__main__':
    result = add_year_and_day(datetime(2020, 12, 31))
    print(result)