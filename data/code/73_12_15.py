SECONDS_PER_HOUR = 3600

def time_difference_in_hours(start_time, end_time):
    return (end_time - start_time) / SECONDS_PER_HOUR
if __name__ == '__main__':
    print(time_difference_in_hours(1672531200.0, 1672560000.0))