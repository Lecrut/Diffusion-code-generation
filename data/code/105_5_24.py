from datetime import date, timedelta
from collections import OrderedDict

DAY_NAMES = OrderedDict([
    ("MONDAY", 0),
    ("TUESDAY", 1),
    ("WEDNESDAY", 2),
    ("THURSDAY", 3),
    ("FRIDAY", 4),
    ("SATURDAY", 5),
    ("SUNDAY", 6)
])

def get_next_weekday(current: date, target: str) -> date:
    target_idx = DAY_NAMES[target]
    current_idx = current.weekday()
    diff = target_idx - current_idx
    if diff <= 0:
        diff += 7
    return current + timedelta(days=diff)

if __name__ == '__main__':
    base_date = date(2023, 10, 10)
    target_day = "WEDNESDAY"
    result = get_next_weekday(base_date, target_day)
    print(result)