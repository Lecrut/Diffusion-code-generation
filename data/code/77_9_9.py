from datetime import datetime
def time_to_minutes(time_str: str) -> int:
    time_str = time_str.lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = time_str.split()
        if len(parts) == 2:
            try:
                hours = int(parts[0].replace('h', ''))
                minutes = int(parts[1].replace('m', ''))
                return hours * 60 + minutes
            except ValueError:
                pass
    try:
        if ':' in time_str:
            if 'h' not in time_str and 'm' not in time_str:
                h, m = map(int, time_str.split(':'))
                return h * 60 + m
        if 'h' in time_str:
            parts = time_str.replace('h', ':').replace('m', ':').split(':')
            if len(parts) == 2:
                h = int(parts[0])
                m = int(parts[1])
                return h * 60 + m
        if 'm' in time_str:
            try:
                minutes = int(time_str.replace('m', ''))
                return minutes
            except ValueError:
                pass
        try:
            t = datetime.strptime(time_str, '%H:%M')
            return t.hour * 60 + t.minute
        except ValueError:
            pass
    except Exception:
        pass
    raise ValueError(f"Could not reliably parse time format: {time_str}")
if __name__ == '__main__':
    test_times = [
        '10:30',
        '14h30m',
        '9:00',
        '23:59',
        '1h30m',
        '5h',
        '30m',
        '12:00'
    ]
    print("--- Time Conversion Tests ---")
    for time_str in test_times:
        try:
            minutes = time_to_minutes(time_str)
            print(f"Input: '{time_str}' -> Total Minutes: {minutes}")
        except ValueError as e:
            print(f"Input: '{time_str}' -> ERROR: {e}")
        print("-" * 20)