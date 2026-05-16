import re
def time_to_minutes(time_str):
    total_minutes = 0
    if not time_str:
        return 0
    time_str = time_str.lower().strip()
    match_hm = re.match(r'(\d{1,2}):(\d{2})', time_str)
    if match_hm:
        hours = int(match_hm.group(1))
        minutes = int(match_hm.group(2))
        total_minutes = hours * 60 + minutes
        return total_minutes
    match_hhm = re.match(r'(\d+)[hH](\d+)[mM]', time_str)
    if match_hhm:
        hours = int(match_hhm.group(1))
        minutes = int(match_hhm.group(2))
        total_minutes = hours * 60 + minutes
        return total_minutes
    match_ms = re.match(r'(\d{1,2}):(\d{2})', time_str)
    if match_ms:
        hours = int(match_ms.group(1))
        minutes = int(match_ms.group(2))
        total_minutes = hours * 60 + minutes
        return total_minutes
    return None
if __name__ == '__main__':
    test_times = [
        '10:30',
        '14h45m',
        '23:59',
        '5h15m',
        '01:00',
        '12:00',
        '9h30',
        '11:59'
    ]
    print("--- Time Conversion Tests ---")
    for time_str in test_times:
        minutes = time_to_minutes(time_str)
        if minutes is not None:
            print(f"Input: '{time_str}' -> Total Minutes: {minutes}")
        else:
            print(f"Input: '{time_str}' -> Conversion Failed (Unrecognized format)")