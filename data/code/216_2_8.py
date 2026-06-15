import math
def find_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"List: {sample_list1}")
    median1 = find_median(sample_list1)
    print(f"Median: {median1}")
    sample_list2 = [10.0, 5.0, 2.0, 8.0, 1.0]
    print(f"\nList: {sample_list2}")
    median2 = find_median(sample_list2)
    print(f"Median: {median2}")
    sample_list3 = [7.0, 7.0, 7.0, 7.0]
    print(f"\nList: {sample_list3}")
    median3 = find_median(sample_list3)
    print(f"Median: {median3}")
    sample_list4 = [1.5, 2.5, 3.5, 4.5]
    print(f"\nList: {sample_list4}")
    median4 = find_median(sample_list4)
    print(f"Median: {median4}")