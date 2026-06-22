from datetime import date

def is_weekend(day):
    return day.weekday() >= 5
if __name__ == '__main__':
    sample_date = date(2023, 10, 7)
    print(is_weekend(sample_date))
    sample_date = date(2023, 10, 8)
    print(is_weekend(sample_date))
    sample_date = date(2023, 10, 9)
    print(is_weekend(sample_date))