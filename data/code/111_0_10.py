import datetime

def days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    print(f"Days between January 1, 2023 and December 31, 2023: {days_between(start_date, end_date)}")