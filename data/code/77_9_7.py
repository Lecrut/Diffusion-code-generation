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
        return h * 60 + m
    raise ValueError(f"Unsupported time format: {time_str}")
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('2:00', 120),
        ('14h30m', 870),
        ('9:5', 545),
        ('01:05', 65),
        ('23:59', 1439),
        ('10h30m', 630),
        ('5h', 300),
        ('30m', 30),
        ('12:00:00', 7200),
    ]
    for input_time, expected in test_cases:
        try:
            result = time_to_minutes(input_time)
            assert result == expected, f"Input: {input_time}, Expected: {expected}, Got: {result}"
            print(f"Input: {input_time} -> Result: {result} (PASS)")
        except ValueError as e:
            print(f"Input: {input_time} -> Error: {e} (FAIL)")
        except AssertionError as e:
            print(f"Assertion Failed for {input_time}: {e}")
        print("-" * 20)