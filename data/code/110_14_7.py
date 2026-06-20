from datetime import datetime

def sort_timestamps_desc(timestamps):
    return sorted(timestamps, reverse=True)

if __name__ == '__main__':
    sample_timestamps = [
        datetime(2023, 10, 5),
        datetime(2023, 9, 15),
        datetime(2023, 11, 20)
    ]
    sorted_timestamps = sort_timestamps_desc(sample_timestamps)
    print(sorted_timestamps)