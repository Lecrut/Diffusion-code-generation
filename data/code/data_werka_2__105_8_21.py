from datetime import date, timedelta

WEEKDAY_MAP = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

def validate_weekday_name(name):
    if name not in WEEKDAY_MAP:
        raise ValueError(f"Unsupported weekday name: {name}")
    return WEEKDAY_MAP[name]

def find_next_weekday(target_weekday_name, initial_date):
    target_index = validate_weekday_name(target_weekday_name)
    current_index = initial_date.weekday()
    difference = target_index - current_index
    if difference <= 0:
        difference += 7
    return initial_date + timedelta(days=difference)

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_day = "thursday"
    result_date = find_next_weekday(target_day, start_date)
    print(result_date)