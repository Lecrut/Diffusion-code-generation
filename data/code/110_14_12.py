from datetime import datetime

def sort_timestamps(timestamps):
    return sorted(timestamps, reverse=True)

if __name__ == '__main__':
    sample_timestamps = [
        datetime(2023, 10, 1),
        datetime(2023, 9, 15),
        datetime(2023, 11, 20)
    ]
    sorted_timestamps = sort_timestamps(sample_timestamps)
    print(sorted_timestamps)