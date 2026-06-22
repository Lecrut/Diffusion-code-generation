import calendar
from datetime import date

WEEKDAY_LABELS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def check_weekday(d):
    try:
        day_index = calendar.weekday(d.year, d.month, d.day)
        is_weekday = day_index < 5
        label = WEEKDAY_LABELS.get(day_index, "Unknown")
        return {
            "date": d,
            "is_weekday": is_weekday,
            "day_name": label,
            "weekday_index": day_index,
        }
    except AttributeError:
        return {
            "date": d,
            "is_weekday": False,
            "day_name": "Unknown",
            "weekday_index": -1,
        }

if __name__ == '__main__':
    test_date = date(2023, 10, 23)
    outcome = check_weekday(test_date)
    print(outcome)