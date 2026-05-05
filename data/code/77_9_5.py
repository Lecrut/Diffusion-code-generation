from datetime import datetime
def time_to_minutes(time_str: str) -> int:
    time_str = time_str.lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = time_str.split('h')
        if len(parts) == 2:
            hours = float(parts[0])
            minutes = float(parts[1].replace('m', ''))
            total_minutes = hours * 60 + minutes
            return int(total_minutes)
        elif 'm' in time_str:
            parts = time_str.split('m')
            if len(parts) == 2:
                hours = float(parts[0].replace('h', ''))
                minutes = float(parts[1])
                total_minutes = hours * 60 + minutes
                return int(total_minutes)
    try:
        if ':' in time_str:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        else:
            if len(time_str) == 4 and time_str.isdigit():
                h = int(time_str[:2])
                m = int(time_str[2:])
                return h * 60 + m
            raise ValueError("Invalid time format")
    except ValueError:
        raise ValueError(f"Could not parse time string: {time_str}")
if __name__ == '__main__':
    test_times = [
        '10:30',
        '14:05',
        '23:59',
        '10h30m',
        '2h15m',
        '5:0',
        '1230'
    ]
    for t in test_times:
        try:
            minutes = time_to_minutes(t)
            print(f"Input: '{t}' -> Total Minutes: {minutes}")
        except ValueError as e:
            print(f"Input: '{t}' -> Error: {e}")
        print("-" * 20)