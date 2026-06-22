HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * SECONDS_IN_MINUTE * MINUTES_IN_HOUR + minutes * SECONDS_IN_MINUTE + seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY)
    remaining_seconds = total_seconds % (SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY)
    hours = remaining_seconds // (SECONDS_IN_MINUTE * MINUTES_IN_HOUR)
    remaining_seconds %= (SECONDS_IN_MINUTE * MINUTES_IN_HOUR)
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    seconds = remaining_seconds % SECONDS_IN_MINUTE
    return f"{days} days, {hours} hours, {minutes} minutes"

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '72:45:30'
    result = convert_time(sample_time)
    print(result)