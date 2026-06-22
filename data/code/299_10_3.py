from datetime import date

def is_weekend(year, month, day):
    target_date = date(year, month, day)
    return target_date.weekday() >= 5
if __name__ == '__main__':
    sample_date1 = date(2023, 10, 7)
    sample_date2 = date(2023, 10, 8)
    print(is_weekend(sample_date1.year, sample_date1.month, sample_date1.day))
    print(is_weekend(sample_date2.year, sample_date2.month, sample_date2.day))