from datetime import timedelta

TIME_UNITS = {
    'seconds_per_minute': 60,
    'minutes_per_hour': 60,
    'hours_per_day': 24,
    'days_per_year': 365
}

def compute_year_seconds():
    seconds_per_day = (TIME_UNITS['minutes_per_hour'] * TIME_UNITS['seconds_per_minute']) * TIME_UNITS['hours_per_day']
    total_seconds = seconds_per_day * TIME_UNITS['days_per_year']
    return total_seconds

if __name__ == '__main__':
    result = compute_year_seconds()
    print(result)