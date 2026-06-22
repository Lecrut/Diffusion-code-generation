from datetime import date, timedelta
import calendar

_TARGET_WEEKDAY = 2

def next_weekday_from(start: date, target: int) -> date:
    days_to_add = (target - start.weekday()) % 7
    if days_to_add == 0:
        return start + timedelta(days=7)
    return start + timedelta(days=days_to_add)

def get_next_wednesday(start: date) -> date:
    if start.weekday() == _TARGET_WEEKDAY:
        return start + timedelta(days=7)
    delta = (_TARGET_WEEKDAY - start.weekday() + 7) % 7
    return start + timedelta(days=delta)

if __name__ == '__main__':
    start = date(2023, 10, 10)
    result = get_next_wednesday(start)
    print(result)