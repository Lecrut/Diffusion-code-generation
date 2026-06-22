SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def convert_seconds_to_dhms(total_seconds):
    days = total_seconds // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY)
    hours = (total_seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY)) // (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)
    minutes = (total_seconds % (SECONDS_PER_MINUTE * MINUTES_PER_HOUR)) // SECONDS_PER_MINUTE
    seconds = total_seconds % SECONDS_PER_MINUTE
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_duration = 1234567
    days, hours, minutes, seconds = convert_seconds_to_dhms(sample_duration)
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")