import datetime

DAY_MAP = {
    1: 1,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def extract_day(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a date object")
    day = date_obj.day
    return day

if __name__ == '__main__':
    target_date = datetime.date(2023, 3, 15)
    computed_day = extract_day(target_date)
    print(computed_day)