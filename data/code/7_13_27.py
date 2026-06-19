def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes"

if __name__ == '__main__':
    time_str = "12:34:56"
    total_seconds = time_to_seconds(time_str)
    human_readable_time = seconds_to_human_readable(total_seconds)
    print(human_readable_time)