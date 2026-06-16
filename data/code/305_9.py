from datetime import datetime
def sort_datetimes_by_date(datetime_list):
    return sorted(datetime_list, key=lambda dt: dt.date())
if __name__ == '__main__':
    list1 = [
        datetime(2023, 10, 27, 10, 30),
        datetime(2023, 10, 25, 15, 45),
        datetime(2023, 10, 28, 9, 0),
    ]
    list2 = [
        datetime(2024, 1, 1, 0, 0),
        datetime(2023, 12, 31, 23, 59),
        datetime(2024, 1, 2, 1, 1),
    ]
    print("List 1 sorted:")
    sorted_list1 = sort_datetimes_by_date(list1)
    for dt in sorted_list1:
        print(dt)
    print("\nList 2 sorted:")
    sorted_list2 = sort_datetimes_by_date(list2)
    for dt in sorted_list2:
        print(dt)