from datetime import datetime, timedelta

WEEKDAY_NAMES = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

def find_next_weekday(target_name, start_str):
    if target_name not in WEEKDAY_NAMES:
        raise ValueError(f"Unknown weekday: {target_name}")
    
    target_idx = WEEKDAY_NAMES[target_name]
    start_dt = datetime.strptime(start_str, '%Y-%m-%d')
    current_idx = start_dt.weekday()
    
    diff = target_idx - current_idx
    if diff <= 0:
        diff += 7
    
    result_dt = start_dt + timedelta(days=diff)
    return result_dt.strftime('%Y-%m-%d')

if __name__ == '__main__':
    output = find_next_weekday('friday', '2023-10-01')
    print(output)