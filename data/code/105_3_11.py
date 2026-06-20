from datetime import date, timedelta

def next_15th_day_of_month(given_date):
    year = given_date.year
    month = given_date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    target_date = date(year, month, 1)
    while target_date.day < 15:
        target_date += timedelta(days=1)
    return target_date

if __name__ == '__main__':
    sample_date = date(2023, 3, 3)
    result = next_15th_day_of_month(sample_date)
    print(result)