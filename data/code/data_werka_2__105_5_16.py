from datetime import date, timedelta

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

TARGET_WEEKDAY = 2

def find_next_weekday(target_day: int, start: date) -> date:
    current_weekday = start.weekday()
    days_until_target = (target_day - current_weekday) % 7
    if days_until_target == 0:
        days_until_target = 7
    return start + timedelta(days=days_until_target)

if __name__ == '__main__':
    start_date = date(2023, 10, 10)
    next_wednesday = find_next_weekday(TARGET_WEEKDAY, start_date)
    print(next_wednesday)