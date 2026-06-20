from datetime import date, timedelta

def next_15th_of_month(hardcoded_date):
    year = hardcoded_date.year
    month = hardcoded_date.month
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 15)

if __name__ == '__main__':
    sample_date = date(2023, 3, 3)
    next_date = next_15th_of_month(sample_date)
    print(next_date)