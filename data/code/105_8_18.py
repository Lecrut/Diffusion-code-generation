from datetime import date, timedelta

WEEKDAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

def find_next_weekday(target_name, start_date):
    target_index = WEEKDAY_MAP.get(target_name)
    if target_index is None:
        raise ValueError(f"Unsupported weekday name: {target_name}")
    
    current_index = start_date.weekday()
    days_diff = target_index - current_index
    if days_diff <= 0:
        days_diff += 7
    
    return start_date + timedelta(days=days_diff)

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_day = "Thursday"
    result = find_next_weekday(target_day, start_date)
    print(result)