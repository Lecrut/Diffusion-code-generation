from datetime import date

def is_weekday(dt):
    return 0 < dt.weekday() < 5
if __name__ == '__main__':
    sample_date = date(2023, 10, 16)
    print(is_weekday(sample_date))