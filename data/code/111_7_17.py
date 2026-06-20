from datetime import datetime, timedelta

def add_year_and_day(date):
    return date + timedelta(days=365) + timedelta(days=1)

if __name__ == '__main__':
    sample_date = datetime(2020, 12, 31)
    result = add_year_and_day(sample_date)
    print(result)