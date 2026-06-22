import datetime

def get_seconds_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - midnight
    return delta.total_seconds()

def convert_to_unit(seconds, units):
    unit_map = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    if units not in unit_map:
        raise ValueError(f"Unsupported unit: {units}")
    return seconds / unit_map[units]

if __name__ == '__main__':
    total_seconds = get_seconds_since_midnight()
    hours_elapsed = convert_to_unit(total_seconds, 'hours')
    minutes_elapsed = convert_to_unit(total_seconds, 'minutes')
    
    print(total_seconds)
    print(hours_elapsed)
    print(minutes_elapsed)