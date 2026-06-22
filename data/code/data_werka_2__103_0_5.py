import datetime

def get_seconds_since_midnight():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - start_of_day
    return delta.total_seconds()

def format_time_elapsed(total_seconds):
    units = {
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }
    remaining = total_seconds
    parts = []
    for unit_name, unit_value in units.items():
        if remaining >= unit_value:
            count = int(remaining // unit_value)
            parts.append(f"{count} {unit_name}")
            remaining -= count * unit_value
    if not parts:
        return "0 seconds"
    return ", ".join(parts)

if __name__ == '__main__':
    elapsed_seconds = get_seconds_since_midnight()
    formatted = format_time_elapsed(elapsed_seconds)
    print(f"{elapsed_seconds} seconds ({formatted})")