def calculate_net_time_difference(time_string, delimiter=';'):
    time_points = []
    if not time_string:
        return 0
    time_segments = time_string.split(delimiter)
    for segment in time_segments:
        try:
            time_points.append(int(segment))
        except ValueError:
            continue
    if not time_points:
        return 0
    min_time = min(time_points)
    max_time = max(time_points)
    return max_time - min_time
if __name__ == '__main__':
    sample_time_string = "10;5;20;15;30"
    result = calculate_net_time_difference(sample_time_string)
    print(result)