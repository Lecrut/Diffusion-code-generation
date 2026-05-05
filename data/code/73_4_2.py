import time
def time_difference(t1, t2):
    return abs(t1 - t2)
if __name__ == '__main__':
    ts1 = 1678886400
    ts2 = 1678890000
    diff = time_difference(ts1, ts2)
    print(diff)