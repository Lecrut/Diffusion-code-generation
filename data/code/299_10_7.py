from datetime import date

def is_weekend(year, month, day):
    return date(year, month, day).weekday() >= 5

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 9
    print(is_weekend(sample_year, sample_month, sample_day))