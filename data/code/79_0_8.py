from datetime import date, timedelta

def next_month(start_date):
    year = start_date.year
    month = start_date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1)

if __name__ == '__main__':
    sample_date = date(2023, 11, 15)
    print(next_month(sample_date))