from datetime import date, timedelta
from calendar import day_name

WEEKDAY_MAP = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

def find_next_weekday(target_name: str, reference: date) -> date:
    target_idx = WEEKDAY_MAP[target_name.lower()]
    current_idx = reference.weekday()
    difference = target_idx - current_idx
    if difference <= 0:
        difference += 7
    return reference + timedelta(days=difference)

if __name__ == '__main__':
    ref_date = date(2023, 9, 15)
    target_day = "thursday"
    computed_date = find_next_weekday(target_day, ref_date)
    print(computed_date)