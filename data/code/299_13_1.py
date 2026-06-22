from datetime import date

def is_weekend(day):
    return day.weekday() >= 5
if __name__ == '__main__':
    sample_date = date(2023, 9, 16)
    print(is_weekend(sample_date))
    sample_date = date(2023, 9, 17)
    print(is_weekend(sample_date))
    sample_date = date(2023, 9, 18)
    print(is_weekend(sample_date))