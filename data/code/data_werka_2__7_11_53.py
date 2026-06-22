def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_days_hours_minutes(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    return days, hours, minutes

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    days, hours, minutes = seconds_to_days_hours_minutes(total_seconds)
    return f"{days} days, {hours} hours, {minutes} minutes"

if __name__ == '__main__':
    sample_time = '01:23:45'
    result = convert_time(sample_time)
    print(result)