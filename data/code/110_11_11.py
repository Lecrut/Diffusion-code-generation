from datetime import datetime

def sort_datetime_list(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 1, 5),
        datetime(2022, 12, 25),
        datetime(2023, 1, 1)
    ]
    print(sort_datetime_list(sample_dates))