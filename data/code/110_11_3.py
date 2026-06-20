from datetime import datetime

def sort_datetime_list(datetime_list):
    return sorted(datetime_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 4, 1),
        datetime(2022, 1, 15),
        datetime(2023, 3, 20)
    ]
    sorted_datetimes = sort_datetime_list(sample_datetimes)
    print(sorted_datetimes)