from datetime import datetime

def sort_datetime_list(date_objects):
    return sorted(date_objects)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 4, 1),
        datetime(2022, 1, 15),
        datetime(2023, 3, 20)
    ]
    sorted_dates = sort_datetime_list(sample_dates)
    print(sorted_dates)