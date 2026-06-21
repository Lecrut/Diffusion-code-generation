import datetime
import functools

def sort_datetimes(datetimes: list[datetime.datetime]) -> list[datetime.datetime]:
    return sorted(datetimes)

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 1, 15, 10, 30, 0)
    dt2 = datetime.datetime(2022, 12, 31, 23, 59, 59)
    dt3 = datetime.datetime(2023, 1, 15, 10, 30, 0)
    dt4 = datetime.datetime(2023, 2, 1, 0, 0, 0)
    
    unsorted_list = [dt1, dt2, dt4, dt3]
    result = sort_datetimes(unsorted_list)
    
    for dt in result:
        print(dt.isoformat())