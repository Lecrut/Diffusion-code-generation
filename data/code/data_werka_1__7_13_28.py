def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes"

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '12:34:56'
    result = convert_time(sample_time)
    print(result)