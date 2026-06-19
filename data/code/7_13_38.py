def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes"

if __name__ == '__main__':
    sample_time_str = '12:45:30'
    total_seconds = time_to_seconds(sample_time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    print(human_readable)