from datetime import datetime

def sort_datetimes(datetimes_list):
    return sorted(datetimes_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 10, 15, 10, 30, 0),
        datetime(2021, 5, 20, 8, 15, 0),
        datetime(2024, 1, 1, 0, 0, 0),
        datetime(2022, 12, 31, 23, 59, 59),
    ]
    sorted_result = sort_datetimes(sample_datetimes)
    print(sorted_result)