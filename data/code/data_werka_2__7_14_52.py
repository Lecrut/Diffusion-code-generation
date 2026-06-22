SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def convert_to_minutes(days=0, hours=0, minutes=0, seconds=0):
    total_seconds = (days * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                    (hours * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                    (minutes * SECONDS_PER_MINUTE) + \
                    seconds
    return total_seconds // SECONDS_PER_MINUTE

if __name__ == '__main__':
    sample_days = 2
    sample_hours = 7
    sample_minutes = 45
    sample_seconds = 30
    result = convert_to_minutes(sample_days, sample_hours, sample_minutes, sample_seconds)
    print(result)