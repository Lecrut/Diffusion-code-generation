from datetime import datetime
import calendar

def is_weekday(dt):
    return dt.weekday() < 5
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5)
    print(is_weekday(sample_dt))