def calculate_time_difference(timestamp1, timestamp2):
    return abs(timestamp2 - timestamp1)

if __name__ == '__main__':
    sample_timestamps = {
        "timestamp1": 1635470400,
        "timestamp2": 1635556800
    }
    time_difference = calculate_time_difference(sample_timestamps["timestamp1"], sample_timestamps["timestamp2"])
    print(f"Time Difference: {time_difference} seconds")