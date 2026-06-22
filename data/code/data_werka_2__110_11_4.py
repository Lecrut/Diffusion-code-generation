from datetime import datetime

def sort_datetimes(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 10, 15, 10, 30),
        datetime(2021, 5, 20, 8, 15),
        datetime(2023, 1, 1, 0, 0),
        datetime(2022, 12, 31, 23, 59),
    ]
    sorted_result = sort_datetimes(sample_datetimes)
    print(sorted_result)