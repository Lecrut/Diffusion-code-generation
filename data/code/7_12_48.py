SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def convert_seconds_to_dhms(seconds):
    days = seconds // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY)
    hours = (seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY)) // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)
    minutes = (seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)) // SECONDS_PER_MINUTE
    remaining_seconds = seconds % SECONDS_PER_MINUTE
    return days, hours, minutes, remaining_seconds

if __name__ == '__main__':
    sample_values = [86401, 90062, 3662, 7201, 1235, 0]
    for value in sample_values:
        print(convert_seconds_to_dhms(value))