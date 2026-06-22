def time_difference(time1: int, time2: int) -> tuple:
    seconds_diff = abs(time2 - time1)
    hours = seconds_diff // 3600
    minutes = (seconds_diff % 3600) // 60
    seconds = seconds_diff % 60
    return (hours, minutes, seconds)

if __name__ == '__main__':
    start_time = 25 * 3600 + 45 * 60 + 30
    end_time = 30 * 3600 + 15 * 60 + 45
    diff = time_difference(start_time, end_time)
    print(f"Time difference: {diff[0]} hours, {diff[1]} minutes, {diff[2]} seconds")