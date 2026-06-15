import math
def calculate_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    print(f"Median of {list1}: {calculate_median(list1)}")
    list2 = [4, 1, 3, 6, 2]
    print(f"Median of {list2}: {calculate_median(list2)}")
    list3 = [5, 2, 8, 1, 9]
    print(f"Median of {list3}: {calculate_median(list3)}")
    list4 = [10, 20, 30, 40]
    print(f"Median of {list4}: {calculate_median(list4)}")
    list5 = []
    print(f"Median of {list5}: {calculate_median(list5)}")
    list6 = [1, 2, 3, 4, 5, 6]
    print(f"Median of {list6}: {calculate_median(list6)}")