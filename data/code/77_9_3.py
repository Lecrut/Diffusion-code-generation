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
    try:
        if ':' in time_str:
            parts = time_str.split(':')
            if len(parts) == 2:
                hours = int(parts[0])
                minutes = int(parts[1])
                return hours * 60 + minutes
    except ValueError:
        pass
    try:
        if 'm' in time_str:
            minutes = int(re.search(r'(\d+)[m]', time_str).group(1))
            return minutes
        if 'h' in time_str:
            hours = int(re.search(r'(\d+)[h]', time_str).group(1))
            return hours * 60
    except (AttributeError, ValueError):
        pass
    raise ValueError(f"Could not reliably parse time format: {time_str}")
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('14h30m', 870),
        ('2:00', 120),
        ('23:59', 1439),
        ('10h', 600),
        ('30m', 30),
        ('1:0', 60),
        ('10:30 AM', 630),
        ('10h30m', 630),
        ('5:15', 315),
        ('90', 90)
    ]
    for input_str, expected in test_cases:
        try:
            result = time_to_minutes(input_str)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected})"
            print(f"Input: '{input_str}' -> Result: {result} ({status})")
        except ValueError as e:
            print(f"Input: '{input_str}' -> ERROR: {e}")
        except Exception as e:
            print(f"Input: '{input_str}' -> UNEXPECTED ERROR: {e}")