import datetime

DAYS_IN_YEAR = 365
START_DATE = datetime.date(2023, 1, 1)
END_DATE = datetime.date(2023, 12, 31)

def days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    print(f"Days between {START_DATE} and {END_DATE}: {days_between(START_DATE, END_DATE)}")