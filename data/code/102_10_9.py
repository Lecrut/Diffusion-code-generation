import calendar
from datetime import datetime

def is_weekday(date_obj):
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 24)
    print(is_weekday(sample_date))