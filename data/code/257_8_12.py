def time_diff(time1, time2):
    hours1, minutes1, seconds1 = time1
    hours2, minutes2, seconds2 = time2
    total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
    total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
    diff_seconds = abs(total_seconds1 - total_seconds2)
    hours_diff = diff_seconds // 3600
    minutes_diff = diff_seconds % 3600 // 60
    seconds_diff = diff_seconds % 60
    return (hours_diff, minutes_diff, seconds_diff)
if __name__ == '__main__':
    sample_time1 = (2, 45, 30)
    sample_time2 = (1, 30, 15)
    result = time_diff(sample_time1, sample_time2)
    print(result)