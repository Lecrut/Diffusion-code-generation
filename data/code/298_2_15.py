def time_difference(time1: int, time2: int) -> tuple:
    seconds_diff = abs(time2 - time1)
    hours = seconds_diff // 3600
    minutes = (seconds_diff % 3600) // 60
    seconds = seconds_diff % 60
    return (hours, minutes, seconds)

if __name__ == '__main__':
    start_time = 2500
    end_time = 7800
    diff = time_difference(start_time, end_time)
    print(f"Time difference between {start_time} and {end_time} is {diff[0]} hours, {diff[1]} minutes, and {diff[2]} seconds")