def time_difference_in_hours(start_time: float, end_time: float) -> float:
    seconds_per_hour = 3600
    time_difference_seconds = abs(end_time - start_time)
    hours = time_difference_seconds / seconds_per_hour
    return hours
if __name__ == '__main__':
    start_timestamp = 1672531200.0
    end_timestamp = 1672617600.0
    difference = time_difference_in_hours(start_timestamp, end_timestamp)
    print(difference)