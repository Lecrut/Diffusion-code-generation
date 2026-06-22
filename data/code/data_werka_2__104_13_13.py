import datetime
import calendar

_WEEK_MAPPING = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def _get_iso_week_key(d: datetime.date) -> tuple:
    iso_data = d.isocalendar()
    return (iso_data[0], iso_data[1])

def check_same_week(date_first: datetime.date, date_second: datetime.date) -> bool:
    if not isinstance(date_first, datetime.date):
        raise ValueError("date_first must be a datetime.date object")
    if not isinstance(date_second, datetime.date):
        raise ValueError("date_second must be a datetime.date object")
    
    key_first = _get_iso_week_key(date_first)
    key_second = _get_iso_week_key(date_second)
    
    return key_first == key_second

if __name__ == '__main__':
    start_of_week = datetime.date(2023, 1, 2)
    end_of_week = datetime.date(2023, 1, 8)
    next_week_start = datetime.date(2023, 1, 9)
    
    result_1 = check_same_week(start_of_week, end_of_week)
    result_2 = check_same_week(start_of_week, next_week_start)
    
    print(result_1)
    print(result_2)