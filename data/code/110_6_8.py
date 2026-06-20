import time

SORT_KEY = lambda ts: time.localtime(ts)

def sort_timestamps(timestamps):
    return sorted(timestamps, key=SORT_KEY)

if __name__ == '__main__':
    sample_timestamps = [1633024800, 1633111200, 1632938400]
    print(sort_timestamps(sample_timestamps))