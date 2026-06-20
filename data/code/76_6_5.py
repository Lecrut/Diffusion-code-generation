from datetime import date, timedelta

def days_between_dates(date1, date2):
    delta = abs(date2 - date1)
    return delta.days

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 12, 31)
    print(days_between_dates(sample_date1, sample_date2))