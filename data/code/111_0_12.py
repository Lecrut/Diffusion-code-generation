import datetime

START_DATE = datetime.date(2023, 1, 1)
END_DATE = datetime.date(2023, 12, 31)

def days_between_dates(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    days_count = days_between_dates(START_DATE, END_DATE)
    print(f"Number of days between {START_DATE} and {END_DATE}: {days_count}")