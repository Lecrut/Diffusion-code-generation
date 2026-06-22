def validate_time(time_tuple):
    hours, minutes, seconds = time_tuple
    if not (0 <= hours < 24 and 0 <= minutes < 60 and (0 <= seconds < 60)):
        raise ValueError('Invalid time format. Hours must be between 0 and 23, minutes and seconds between 0 and 59.')

def calculate_time_difference(time1, time2):
    validate_time(time1)
    validate_time(time2)
    hours_diff = time1[0] - time2[0]
    minutes_diff = time1[1] - time2[1]
    seconds_diff = time1[2] - time2[2]
    if seconds_diff < 0:
        minutes_diff -= 1
        seconds_diff += 60
    if minutes_diff < 0:
        hours_diff -= 1
        minutes_diff += 60
    return (hours_diff, minutes_diff, seconds_diff)
if __name__ == '__main__':
    time1 = (3, 45, 20)
    time2 = (2, 10, 10)
    result = calculate_time_difference(time1, time2)
    print(result)