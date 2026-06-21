def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_human_readable(total_seconds):
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60
    
    days = total_seconds // SECONDS_IN_DAY
    remaining_seconds = total_seconds % SECONDS_IN_DAY
    
    hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds %= SECONDS_IN_HOUR
    
    minutes = remaining_seconds // SECONDS_IN_MINUTE
    seconds = remaining_seconds % SECONDS_IN_MINUTE
    
    return f"{days} days, {hours} hours, {minutes} minutes"

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '07:45:30'
    result = convert_time(sample_time)
    print(result)