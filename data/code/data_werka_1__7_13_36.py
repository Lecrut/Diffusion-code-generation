def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes"

if __name__ == '__main__':
    sample_time = "12:34:56"
    total_seconds = time_to_seconds(sample_time)
    human_readable = seconds_to_human_readable(total_seconds)
    print(human_readable)