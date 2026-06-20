def calculate_time_difference(timestamp1, timestamp2):
    if timestamp2 > timestamp1:
        time_difference = timestamp2 - timestamp1
    else:
        time_difference = timestamp1 - timestamp2
    return abs(time_difference)
if __name__ == '__main__':
    sample_timestamp1 = 1698086400
    sample_timestamp2 = 1698172800
    result = calculate_time_difference(sample_timestamp1, sample_timestamp2)
    print(f'Time Difference in Seconds: {result}')