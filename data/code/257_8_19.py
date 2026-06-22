def time_difference(time1, time2):
    hours_diff = abs(time1[0] - time2[0])
    minutes_diff = abs(time1[1] - time2[1])
    seconds_diff = abs(time1[2] - time2[2])
    return (hours_diff, minutes_diff, seconds_diff)

if __name__ == '__main__':
    print(time_difference((3, 45, 20), (2, 30, 10)))