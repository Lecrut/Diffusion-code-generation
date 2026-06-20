from datetime import date, timedelta

def nearest_saturday(target_date):
    days_until_saturday = (5 - target_date.weekday()) % 7
    return target_date + timedelta(days=days_until_saturday)

if __name__ == '__main__':
    sample_date = date(2023, 11, 1)
    print(nearest_saturday(sample_date))