from datetime import datetime

def sort_datetime_list(datetime_list):
    return sorted(datetime_list)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 4, 1),
        datetime(2023, 3, 15),
        datetime(2023, 5, 10)
    ]
    sorted_dates = sort_datetime_list(sample_dates)
    print(sorted_dates)