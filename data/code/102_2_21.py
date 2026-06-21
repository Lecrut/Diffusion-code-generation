import datetime

WEEKDAY_START = 0
WEEKDAY_END = 5

def is_weekday(date_obj):
    day_index = date_obj.weekday()
    is_within_range = day_index >= WEEKDAY_START
    is_not_weekend = day_index < WEEKDAY_END
    return is_within_range and is_not_weekend

if __name__ == '__main__':
    test_date = datetime.date(2023, 10, 25)
    is_work_day = is_weekday(test_date)
    print(is_work_day)