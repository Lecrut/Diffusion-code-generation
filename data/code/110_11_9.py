from datetime import datetime

def sort_datetimes(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 15, 10, 30),
        datetime(2021, 5, 20, 8, 0),
        datetime(2022, 1, 1, 0, 0),
        datetime(2023, 12, 31, 23, 59),
    ]
    sorted_dates = sort_datetimes(sample_dates)
    print(sorted_dates)