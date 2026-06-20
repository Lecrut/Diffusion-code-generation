from datetime import date

def days_between_dates(date1, date2):
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    sample_date1 = date(2023, 8, 1)
    sample_date2 = date(2023, 8, 15)
    print(days_between_dates(sample_date1, sample_date2))