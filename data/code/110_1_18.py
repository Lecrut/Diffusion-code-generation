from datetime import datetime

def sort_datetimes(datetimes_list):
    return sorted(datetimes_list)

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2022, 12, 31)
    dt3 = datetime(2023, 6, 15)
    unsorted_list = [dt1, dt2, dt3]
    sorted_list = sort_datetimes(unsorted_list)
    print(sorted_list)