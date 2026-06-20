from datetime import datetime

def sort_dates():
    dates = [
        datetime(2023, 1, 15),
        datetime(2022, 12, 31),
        datetime(2023, 5, 20),
        datetime(2021, 10, 10)
    ]
    sorted_dates = sorted(dates)
    return sorted_dates

if __name__ == '__main__':
    print(sort_dates())