from datetime import datetime
def sort_datetimes(dt_list):
    return sorted(dt_list, key=lambda dt: (dt.year, dt.month, dt.day))
if __name__ == '__main__':
    dates = [
        datetime(2023, 10, 25),
        datetime(2022, 1, 15),
        datetime(2023, 10, 1),
        datetime(2022, 1, 1),
        datetime(2023, 10, 25),
        datetime(2022, 1, 1),
    ]
    sorted_dates = sort_datetimes(dates)
    for dt in sorted_dates:
        print(dt)