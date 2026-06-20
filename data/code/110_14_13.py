from datetime import datetime

def sort_timestamps(timestamps):
    return sorted(timestamps, reverse=True)

if __name__ == '__main__':
    sample_timestamps = [
        datetime(2023, 10, 15, 12, 0),
        datetime(2023, 9, 20, 14, 30),
        datetime(2023, 11, 10, 8, 15)
    ]
    sorted_timestamps = sort_timestamps(sample_timestamps)
    print(sorted_timestamps)