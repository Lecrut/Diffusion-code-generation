import time
def calculate_time_difference(timestamp1: int, timestamp2: int) -> int:
    if timestamp1 > timestamp2:
        return timestamp1 - timestamp2
    else:
        return timestamp2 - timestamp1
if __name__ == '__main__':
    ts1 = 1678886400
    ts2 = 1678972800
    difference = calculate_time_difference(ts1, ts2)
    print(difference)