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
    list2 = [3, 7, 1, 4, 6, 2]
    list3 = [10, 20, 30, 40]
    median1 = calculate_median(list1)
    print(f"Median of {list1}: {median1}")
    median2 = calculate_median(list2)
    print(f"Median of {list2}: {median2}")
    median3 = calculate_median(list3)
    print(f"Median of {list3}: {median3}")