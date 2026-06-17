from datetime import datetime
def sort_datetimes_by_date(datetimes):
    return sorted(datetimes, key=lambda dt: dt.date())
if __name__ == '__main__':
    list1 = [
        datetime(2023, 10, 27, 14, 30),
        datetime(2023, 10, 25, 9, 0),
        datetime(2023, 10, 28, 10, 0)
    ]
    list2 = [
        datetime(2024, 1, 1, 0, 0),
        datetime(2023, 12, 31, 23, 59),
        datetime(2024, 1, 2, 1, 1)
    ]
    list3 = [
        datetime(2023, 10, 27, 10, 0),
        datetime(2023, 10, 27, 15, 0),
        datetime(2023, 10, 26, 10, 0)
    ]
    sorted_list1 = sort_datetimes_by_date(list1)
    print("Sorted List 1:")
    for dt in sorted_list1:
        print(dt)
    sorted_list2 = sort_datetimes_by_date(list2)
    print("\nSorted List 2:")
    for dt in sorted_list2:
        print(dt)
    sorted_list3 = sort_datetimes_by_date(list3)
    print("\nSorted List 3:")
    for dt in sorted_list3:
        print(dt)