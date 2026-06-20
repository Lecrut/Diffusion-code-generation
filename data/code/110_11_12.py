import datetime

def validate_input(date_objects):
    if not all(isinstance(date_obj, datetime.datetime) for date_obj in date_objects):
        raise ValueError("All elements must be datetime objects")

def sort_datetime_list(datetime_list):
    validate_input(datetime_list)
    return sorted(datetime_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime.datetime(2023, 4, 1),
        datetime.datetime(2022, 1, 15),
        datetime.datetime(2023, 3, 20)
    ]
    sorted_datetimes = sort_datetime_list(sample_datetimes)
    print(sorted_datetimes)