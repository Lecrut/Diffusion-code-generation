import math
def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [10, 4, 7, 3, 1]
    list3 = [1, 2, 3, 4, 5, 6]
    list4 = [1, 2, 3, 4]
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    print(f"Median of {list4}: {calculate_median(list4)}")