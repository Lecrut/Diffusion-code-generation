from datetime import datetime
def sort_datetimes(dt_list):
    return sorted(dt_list, key=lambda dt: (dt.year, dt.month, dt.day))
if __name__ == '__main__':
    date1 = datetime(2023, 10, 25)
    date2 = datetime(2022, 1, 15)
    date3 = datetime(2023, 10, 25)
    date4 = datetime(2023, 10, 1)
    date5 = datetime(2022, 10, 31)
    unsorted_list = [date1, date2, date3, date4, date5]
    sorted_list = sort_datetimes(unsorted_list)
    print(sorted_list)