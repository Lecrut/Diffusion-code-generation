from datetime import datetime

def sort_datetime_list(datetime_list):
    return sorted(datetime_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2023, 5, 10),
        datetime(2022, 7, 25),
        datetime(2023, 8, 15)
    ]
    sorted_datetimes = sort_datetime_list(sample_datetimes)
    print(sorted_datetimes)