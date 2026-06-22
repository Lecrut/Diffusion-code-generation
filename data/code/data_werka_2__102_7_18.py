import calendar
from datetime import date

DAY_TYPE_MAP = {
    0: "weekday",
    1: "weekday",
    2: "weekday",
    3: "weekday",
    4: "weekday",
    5: "weekend",
    6: "weekend",
}

def classify_day(d):
    try:
        day_code = calendar.weekday(d.year, d.month, d.day)
        return DAY_TYPE_MAP.get(day_code, "unknown")
    except AttributeError:
        return "invalid"

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    classification = classify_day(test_date)
    print(classification)