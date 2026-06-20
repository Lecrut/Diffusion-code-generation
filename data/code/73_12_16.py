def time_diff(start_time, end_time):
    start_seconds = int(start_time)
    end_seconds = int(end_time)
    difference_seconds = abs(end_seconds - start_seconds)
    difference_hours = difference_seconds / 3600.0
    return difference_hours
if __name__ == '__main__':
    result = time_diff(1672531200, 1672617600)
    print(result)