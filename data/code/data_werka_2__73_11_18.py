UNIT_MULTIPLIERS = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
    'weeks': 604800
}

def get_time_difference_hours(timestamp_a, timestamp_b):
    if not isinstance(timestamp_a, (int, float)) or not isinstance(timestamp_b, (int, float)):
        raise ValueError("Inputs must be numeric timestamps")
    
    diff_seconds = timestamp_a - timestamp_b
    divisor = UNIT_MULTIPLIERS['hours']
    
    return diff_seconds / divisor

if __name__ == '__main__':
    start_ts = 1609459200
    end_ts = 1609466400
    output = get_time_difference_hours(start_ts, end_ts)
    print(output)