from datetime import date, timedelta

def add_year_and_day(start_date):
    return start_date.replace(year=start_date.year + 1) + timedelta(days=1)

if __name__ == '__main__':
    result = add_year_and_day(date(2020, 12, 31))
    print(result)