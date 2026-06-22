def time_difference(time1_str, time2_str):
    time1 = tuple(map(int, time1_str.split(':')))
    time2 = tuple(map(int, time2_str.split(':')))
    total_seconds1 = time1[0] * 3600 + time1[1] * 60
    total_seconds2 = time2[0] * 3600 + time2[1] * 60
    difference_seconds = abs(total_seconds1 - total_seconds2)
    hours = difference_seconds // 3600
    minutes = (difference_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"

if __name__ == '__main__':
    time_a = "14:30"
    time_b = "17:45"
    result = time_difference(time_a, time_b)
    print(result)