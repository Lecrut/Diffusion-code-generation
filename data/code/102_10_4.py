import datetime

def is_weekday(dt):
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 15)
    print(is_weekday(sample_dt))