def calculate_time_difference(timestamp1, timestamp2):
    difference = abs(timestamp2 - timestamp1)
    return int(difference)
if __name__ == '__main__':
    start_timestamp = 1698038400
    end_timestamp = 1698124800
    result = calculate_time_difference(start_timestamp, end_timestamp)
    print(f'Time Difference in Seconds: {result}')