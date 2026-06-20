from datetime import date

def days_between_dates(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    print(days_between_dates(start_date, end_date))