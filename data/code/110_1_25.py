from datetime import datetime

def sort_datetime_list(dt_list):
    if not all(isinstance(item, datetime) for item in dt_list):
        raise ValueError("All items in the list must be instances of datetime.")
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 1, 5),
        datetime(2022, 12, 25),
        datetime(2023, 1, 1)
    ]
    try:
        sorted_dates = sort_datetime_list(sample_dates)
        print(sorted_dates)
    except ValueError as e:
        print(e)