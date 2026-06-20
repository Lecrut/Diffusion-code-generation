import time

def time_difference_in_hours(timestamp1, timestamp2):
    return abs((timestamp2 - timestamp1) / 3600)
if __name__ == '__main__':
    sample_timestamp1 = 1672531200.0
    sample_timestamp2 = 1672617600.0
    print(time_difference_in_hours(sample_timestamp1, sample_timestamp2))