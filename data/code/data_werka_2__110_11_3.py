from datetime import datetime

def sort_datetimes(datetimes_list):
    return sorted(datetimes_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 10, 1),
        datetime(2021, 5, 15),
        datetime(2022, 1, 1),
        datetime(2023, 1, 1),
    ]
    sorted_result = sort_datetimes(sample_datetimes)
    print(sorted_result)