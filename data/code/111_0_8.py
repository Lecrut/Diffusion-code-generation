from datetime import date

def days_between_dates(start_date, end_date):
    return (end_date - start_date).days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    print(days_between_dates(start, end))