import math
def find_middle_value(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    list1 = [1, 3, 2]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    list2 = [1, 5, 3, 4, 2]
    print(f"Median of {list2}: {find_middle_value(list2)}")
    list3 = [10, 20, 30, 40]
    print(f"Median of {list3}: {find_middle_value(list3)}")
    list4 = [5]
    print(f"Median of {list4}: {find_middle_value(list4)}")
    list5 = [1, 2, 3, 4, 5, 6]
    print(f"Median of {list5}: {find_middle_value(list5)}")