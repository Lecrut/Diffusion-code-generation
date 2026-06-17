from datetime import datetime
def sort_datetimes_by_date(datetimes):
    return sorted(datetimes, key=lambda dt: dt.date())
if __name__ == '__main__':
    list1 = [datetime(2023, 10, 27, 10, 30), datetime(2023, 10, 25, 15, 0), datetime(2023, 10, 28, 9, 0)]
    list2 = [datetime(2024, 1, 1, 0, 0), datetime(2023, 12, 31, 23, 59), datetime(2024, 1, 2, 1, 1)]
    list3 = [datetime(2023, 5, 15), datetime(2023, 5, 1), datetime(2023, 5, 16)]
    sorted_list1 = sort_datetimes_by_date(list1)
    print("List 1 sorted:")
    for dt in sorted_list1:
        print(dt)
    sorted_list2 = sort_datetimes_by_date(list2)
    print("\nList 2 sorted:")
    for dt in sorted_list2:
        print(dt)
    sorted_list3 = sort_datetimes_by_date(list3)
    print("\nList 3 sorted:")
    for dt in sorted_list3:
        print(dt)