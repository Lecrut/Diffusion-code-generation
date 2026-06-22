from datetime import date, timedelta

WEEKDAY_MAP = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}

def find_next_weekday(target_name, current_date):
    target_idx = WEEKDAY_MAP.get(target_name)
    if target_idx is None:
        raise ValueError(f"Unsupported weekday: {target_name}")
    
    current_idx = current_date.weekday()
    diff = target_idx - current_idx
    
    if diff <= 0:
        diff += 7
    
    return current_date + timedelta(days=diff)

if __name__ == '__main__':
    start = date(2023, 9, 15)
    target = 'Thursday'
    result = find_next_weekday(target, start)
    print(result)