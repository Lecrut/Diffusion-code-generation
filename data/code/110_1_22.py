from datetime import datetime

def sort_datetimes(dates):
    return sorted(dates)

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 10, 1),
        datetime(2021, 5, 15),
        datetime(2022, 1, 1),
        datetime(2024, 12, 31),
        datetime(2020, 7, 4)
    ]
    sorted_dates = sort_datetimes(sample_dates)
    print(sorted_dates)