import datetime
import calendar

def _validate_weekday_index(index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index > 6:
        raise ValueError("Index must be between 0 and 6")
    return True

def get_day_name_from_date(date_obj):
    _validate_weekday_index(date_obj.weekday())
    return calendar.day_name[date_obj.weekday()]

if __name__ == '__main__':
    today = datetime.date.today()
    day_name = get_day_name_from_date(today)
    print(day_name)