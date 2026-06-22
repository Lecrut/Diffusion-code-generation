def time_difference(time1: int, time2: int) -> tuple:
    seconds_diff = abs(time2 - time1)
    hours = seconds_diff // 3600
    minutes = (seconds_diff % 3600) // 60
    seconds = seconds_diff % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    time_a = 4200
    time_b = 1500
    diff = time_difference(time_a, time_b)
    print(f"Time difference: {diff[0]} hours, {diff[1]} minutes, {diff[2]} seconds")