from datetime import datetime

def validate_datetime_list(dt_list):
    if not all(isinstance(item, datetime) for item in dt_list):
        raise ValueError("All elements must be instances of datetime.")

def sort_datetime_list(dt_list):
    validate_datetime_list(dt_list)
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dates = [datetime(2023, 1, 5), datetime(2022, 12, 25), datetime(2023, 1, 1)]
    sorted_dates = sort_datetime_list(sample_dates)
    print(sorted_dates)