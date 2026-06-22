def calculate_difference(time1, time2):
    hours_diff = time1[0] - time2[0]
    minutes_diff = time1[1] - time2[1]
    seconds_diff = time1[2] - time2[2]
    if seconds_diff < 0:
        seconds_diff += 60
        minutes_diff -= 1
    if minutes_diff < 0:
        minutes_diff += 60
        hours_diff -= 1
    if hours_diff < 0:
        hours_diff += 24
    return (hours_diff, minutes_diff, seconds_diff)
if __name__ == '__main__':
    sample_time1 = (15, 30, 45)
    sample_time2 = (18, 45, 15)
    result = calculate_difference(sample_time1, sample_time2)
    print(result)