from datetime import datetime

def sort_timestamps_desc(timestamps):
    return sorted(timestamps, reverse=True)

if __name__ == '__main__':
    sample_timestamps = [
        datetime(2023, 1, 1),
        datetime(2022, 12, 31),
        datetime(2023, 2, 15)
    ]
    sorted_timestamps = sort_timestamps_desc(sample_timestamps)
    print(sorted_timestamps)