from datetime import date

def days_between_dates(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2024, 1, 1)
    print(days_between_dates(sample_date1, sample_date2))