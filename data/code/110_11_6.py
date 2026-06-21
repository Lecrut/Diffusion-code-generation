import datetime
import functools

def sort_datetimes(datetimes):
    return sorted(datetimes)

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 1, 15, 10, 30)
    dt2 = datetime.datetime(2022, 12, 1, 8, 0)
    dt3 = datetime.datetime(2023, 6, 20, 14, 45)
    dt4 = datetime.datetime(2021, 11, 5, 12, 0)
    
    unsorted_list = [dt1, dt2, dt3, dt4]
    sorted_list = sort_datetimes(unsorted_list)
    
    print(sorted_list)