from datetime import date

def days_between_dates(date1: date, date2: date) -> int:
    if date1 > date2:
        date1, date2 = date2, date1
    return (date2 - date1).days

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 12, 31)
    print(days_between_dates(sample_date1, sample_date2))