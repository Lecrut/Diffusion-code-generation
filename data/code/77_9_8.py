import re
def time_to_minutes(time_str):
    time_str = time_str.lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = re.findall(r'(\d+)([hms])', time_str)
        hours = 0
        minutes = 0
        for val, unit in parts:
            if unit == 'h':
                hours += int(val)
            elif unit == 'm':
                minutes += int(val)
        if hours > 0 and minutes > 0:
            return hours * 60 + minutes
        elif hours > 0:
            return hours * 60
        elif minutes > 0:
            return minutes
        else:
            return 0
    if ':' in time_str:
        try:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        except ValueError:
            pass
    try:
        if 'h' in time_str or 'm' in time_str:
            h_match = re.search(r'(\d+)([h])', time_str)
            m_match = re.search(r'(\d+)([m])', time_str)
            if h_match and m_match:
                hours = int(h_match.group(1))
                minutes = int(m_match.group(1))
                return hours * 60 + minutes
            elif h_match:
                hours = int(h_match.group(1))
                return hours * 60
            elif m_match:
                minutes = int(m_match.group(1))
                return minutes
    except Exception:
        pass
    try:
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    except ValueError:
        pass
    return None
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('2:15', 135),
        ('10h30m', 630),
        ('1h30', 90),
        ('2h', 120),
        ('30m', 30),
        ('01:05', 65),
        ('12:00', 720),
        ('10h0m', 600),
        ('5h30m', 330),
        ('45', None),
        ('invalid', None)
    ]
    for input_str, expected in test_cases:
        result = time_to_minutes(input_str)
        print(f"Input: '{input_str}' -> Result: {result}, Expected: {expected}, Match: {result == expected}")
    print("\n--- Additional Test Cases ---")
    print(f"Input: '11:59' -> Result: {time_to_minutes('11:59')}")
    print(f"Input: '12h' -> Result: {time_to_minutes('12h')}")
    print(f"Input: '30' -> Result: {time_to_minutes('30')}")
    print(f"Input: '1h1m' -> Result: {time_to_minutes('1h1m')}")
    print(f"Input: '10:30:00' -> Result: {time_to_minutes('10:30:00')}")