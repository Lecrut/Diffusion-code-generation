from datetime import timedelta

def compute_seconds_in_non_leap_year():
    unit_map = {
        'seconds_per_minute': 60,
        'minutes_per_hour': 60,
        'hours_per_day': 24,
        'days_in_year': 365
    }
    seconds_per_day = (
        unit_map['seconds_per_minute'] *
        unit_map['minutes_per_hour'] *
        unit_map['hours_per_day']
    )
    total_seconds = seconds_per_day * unit_map['days_in_year']
    return total_seconds

if __name__ == '__main__':
    result = compute_seconds_in_non_leap_year()
    print(result)