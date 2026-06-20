from datetime import datetime

def sort_datetime_list(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dt_list = [
        datetime(2023, 4, 1),
        datetime(2023, 3, 31),
        datetime(2023, 5, 1)
    ]
    sorted_dt_list = sort_datetime_list(sample_dt_list)
    print(sorted_dt_list)