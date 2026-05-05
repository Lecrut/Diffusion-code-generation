import re
def time_to_minutes(time_str):
    time_str = time_str.lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = re.findall(r'(\d+)[hhm]', time_str)
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])
            return hours * 60 + minutes
    if ':' in time_str:
        parts = time_str.split(':')
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])
            return hours * 60 + minutes
    try:
        minutes = int(time_str)
        return minutes
    except ValueError:
        return None
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('14h30m', 870),
        ('2:00', 120),
        ('300', 300),
        ('10h', 600),
        ('12:00', 720),
        ('9:5', 545),
        ('250', 250),
        ('1h30m', 90),
    ]
    for time_input, expected in test_cases:
        result = time_to_minutes(time_input)
        print(f"Input: '{time_input}', Result: {result}, Expected: {expected}, Match: {result == expected}")
    print("\n--- Additional Tests ---")
    print(f"Input: '10:30', Result: {time_to_minutes('10:30')}")
    print(f"Input: '14h30m', Result: {time_to_minutes('14h30m')}")
    print(f"Input: '2:00', Result: {time_to_minutes('2:00')}")
    print(f"Input: '300', Result: {time_to_minutes('300')}")
    print(f"Input: '10h', Result: {time_to_minutes('10h')}")
    print(f"Input: '12:00', Result: {time_to_minutes('12:00')}")
    print(f"Input: '9:5', Result: {time_to_minutes('9:5')}")
    print(f"Input: '1h30m', Result: {time_to_minutes('1h30m')}")