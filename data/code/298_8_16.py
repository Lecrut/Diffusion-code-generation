import datetime

def calculate_duration(time_str1, time_str2):
    format_str = '%H:%M'
    time1 = datetime.datetime.strptime(time_str1, format_str)
    time2 = datetime.datetime.strptime(time_str2, format_str)

    if time2 >= time1:
        duration = time2 - time1
    else:
        duration = (time2 + datetime.timedelta(days=1)) - time1

    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    seconds = duration.seconds % 60

    return hours, minutes, seconds

if __name__ == '__main__':
    sample_time_a = "22:00"
    sample_time_b = "06:10"
    result_hours, result_minutes, result_seconds = calculate_duration(sample_time_a, sample_time_b)
    print(f"Duration between {sample_time_a} and {sample_time_b}: {result_hours} hours, {result_minutes} minutes, {result_seconds} seconds")