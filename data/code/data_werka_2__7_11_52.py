HOURS_IN_DAY = 24
SECONDS_IN_HOUR = 3600
MINUTES_IN_HOUR = 60

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * SECONDS_IN_HOUR + minutes * MINUTES_IN_HOUR + seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (HOURS_IN_DAY * SECONDS_IN_HOUR)
    remaining_seconds = total_seconds % (HOURS_IN_DAY * SECONDS_IN_HOUR)
    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds %= SECONDS_IN_HOUR
    minutes = remaining_seconds // MINUTES_IN_HOUR
    seconds = remaining_seconds % MINUTES_IN_HOUR
    return f"{days} days, {hours} hours, {minutes} minutes"

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '25:10:30'
    result = convert_time(sample_time)
    print(result)