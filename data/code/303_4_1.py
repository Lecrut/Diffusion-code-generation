import time
def calculate_time_difference(timestamp1: int, timestamp2: int) -> int:
    return abs(timestamp1 - timestamp2)
if __name__ == '__main__':
    ts1 = 1678886400
    ts2 = 1678972800
    difference = calculate_time_difference(ts1, ts2)
    print(difference)