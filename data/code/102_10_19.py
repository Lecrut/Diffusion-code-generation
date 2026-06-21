import calendar
from datetime import datetime

DAY_TYPE_MAP = {
    0: "weekday",
    1: "weekday",
    2: "weekday",
    3: "weekday",
    4: "weekday",
    5: "weekend",
    6: "weekend",
}

def classify_day(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    return DAY_TYPE_MAP[calendar.weekday(dt.year, dt.month, dt.day)]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    classification = classify_day(sample_date)
    print(classification)
    weekend_date = datetime(2023, 10, 21)
    weekend_classification = classify_day(weekend_date)
    print(weekend_classification)