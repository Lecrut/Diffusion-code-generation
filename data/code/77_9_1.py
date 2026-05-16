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
    if 'h' in time_str or 'm' in time_str:
        try:
            h_match = re.search(r'(\d+)[h]', time_str)
            m_match = re.search(r'(\d+)[m]', time_str)
            if h_match and m_match:
                hours = int(h_match.group(1))
                minutes = int(m_match.group(1))
                return hours * 60 + minutes
        except Exception:
            pass
    try:
        if ':' in time_str:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
    except ValueError:
        pass
    raise ValueError(f"Could not reliably parse time format: {time_str}")
if __name__ == '__main__':
    test_cases = [
        ('10:30', 630),
        ('2:15', 135),
        ('14h30m', 870),
        ('9h5m', 545),
        ('10:00', 600),
        ('01:05', 65),
        ('23:59', 1439),
        ('12h0m', 720),
        ('5h', 300),
        ('30m', 30),
        ('10h30', 630),
        ('11:59', 719)
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
        except Exception as e:
            print(f"Unexpected Error for {input_time}: {e}")