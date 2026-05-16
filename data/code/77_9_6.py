from datetime import datetime
def time_to_minutes(time_str):
    time_str = str(time_str).lower().replace(' ', '')
    if 'h' in time_str or 'm' in time_str:
        parts = time_str.split('h')
        if len(parts) == 2:
            hours = float(parts[0])
            minutes = float(parts[1].replace('m', ''))
            return int(hours * 60 + minutes)
        elif 'm' in time_str:
            parts = time_str.split('m')
            if len(parts) == 2:
                hours = float(parts[0])
                minutes = float(parts[1])
                return int(hours * 60 + minutes)
    try:
        if ':' in time_str:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        else:
            dt = datetime.strptime(time_str, '%H:%M')
            return (dt.hour * 60) + dt.minute
    except ValueError:
        raise ValueError(f"Could not parse time format: {time_str}")
if __name__ == '__main__':
    test_times = [
        '10:30',
        '14:05',
        '23:59',
        '10h30m',
        '2h15m',
        '01:00',
        '11:59'
    ]
    for t in test_times:
        try:
            minutes = time_to_minutes(t)
            print(f"Input: '{t}' -> Total Minutes: {minutes}")
        except ValueError as e:
            print(f"Input: '{t}' -> Error: {e}")