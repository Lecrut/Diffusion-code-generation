from datetime import datetime

def sort_datetime_list(date_objects):
    return sorted(date_objects)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 1, 15),
        datetime(2022, 12, 31),
        datetime(2023, 5, 20),
        datetime(2022, 11, 1)
    ]
    sorted_datetimes = sort_datetime_list(sample_datetimes)
    print(sorted_datetimes)