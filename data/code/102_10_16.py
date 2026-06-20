import datetime

def is_weekday(date_obj):
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_dt = datetime.datetime(2023, 10, 10)
    print(is_weekday(sample_dt))