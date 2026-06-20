from datetime import date

def weeks_between_dates(date1: date, date2: date) -> int:
    delta = abs((date1 - date2).days)
    return delta // 7

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 1, 15)
    print(weeks_between_dates(sample_date1, sample_date2))