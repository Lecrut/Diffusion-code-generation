def time_difference(time1: int, time2: int) -> tuple:
    seconds_diff = abs(time2 - time1)
    hours = seconds_diff // 3600
    minutes = seconds_diff % 3600 // 60
    seconds = seconds_diff % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    print(time_difference(3600, 5400))