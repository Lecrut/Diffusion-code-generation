import re
def time_to_minutes(time_str):
    time_str = str(time_str).lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = re.findall(r'(\d+)[hhm]', time_str)
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])
            return hours * 60 + minutes
        elif len(parts) == 1:
            pass
    if ':' in time_str:
        try:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        except ValueError:
            pass
    if ':' in time_str:
        try:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        except ValueError:
            pass
    match = re.match(r'(\d+)[hhm](\d+)[hhm]?', time_str)
    if match:
        h = int(match.group(1))
        m = int(match.group(2))
        if 'h' in time_str:
            return h * 60 + m
        elif 'm' in time_str:
            return h * 60 + m
    raise ValueError(f"Unsupported time format: {time_str}")
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('14:05', 845),
        ('23:59', 1439),
        ('10h30m', 630),
        ('5h15m', 315),
        ('1h', 60),
        ('30m', 30),
        ('00:00', 0),
        ('12:00', 720),
        ('25h', 1500),
    ]
    for input_time, expected in test_cases:
        try:
            result = time_to_minutes(input_time)
            print(f"Input: '{input_time}' -> Result: {result}, Expected: {expected}, Match: {result == expected}")
        except ValueError as e:
            print(f"Input: '{input_time}' -> Error: {e}")
        except Exception as e:
            print(f"Input: '{input_time}' -> Unexpected Error: {e}")