from datetime import datetime, timedelta

DAY_INDEX = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

def find_next_weekday(reference_str, target_name):
    target_num = DAY_INDEX.get(target_name)
    if target_num is None:
        raise ValueError(f"Unknown weekday: {target_name}")
    ref_date = datetime.strptime(reference_str, '%Y-%m-%d')
    current_num = ref_date.weekday()
    delta = target_num - current_num
    if delta <= 0:
        delta += 7
    next_date = ref_date + timedelta(days=delta)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    start = '2023-10-01'
    day = 'friday'
    output = find_next_weekday(start, day)
    print(output)