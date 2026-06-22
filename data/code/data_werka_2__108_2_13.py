import time
from datetime import datetime

DAY_INDEX = 4
MONTH_INDEX = 1
YEAR_INDEX = 0
HOUR_INDEX = 3

def extract_day_from_structured_time(t_struct):
    return t_struct[DAY_INDEX]

def get_current_day_of_month():
    now = time.localtime()
    return extract_day_from_structured_time(now)

def get_day_from_specific_date(year_val, month_val, day_val):
    try:
        dt_obj = datetime(year_val, month_val, day_val)
        return dt_obj.timetuple()[DAY_INDEX]
    except ValueError:
        return -1

if __name__ == '__main__':
    current_day = get_current_day_of_month()
    print(current_day)

    sample_date_day = get_day_from_specific_date(2023, 10, 15)
    print(sample_date_day)

    leap_year_day = get_day_from_specific_date(2024, 2, 29)
    print(leap_year_day)