from datetime import datetime
def sort_datetimes(dt_list):
    return sorted(dt_list)
if __name__ == '__main__':
    dt_list = [
        datetime(2023, 10, 25),
        datetime(2022, 1, 15),
        datetime(2023, 10, 1),
        datetime(2022, 1, 1),
        datetime(2023, 10, 25),
        datetime(2022, 1, 1),
    ]
    sorted_list = sort_datetimes(dt_list)
    for dt in sorted_list:
        print(dt)