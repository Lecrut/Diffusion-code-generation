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
    sample_list1 = [3.5, 1.0, 4.5, 2.0, 3.0]
    sample_list2 = [7.1, 2.2, 9.8, 4.4, 1.1]
    sample_list3 = [1.0, 5.0, 2.0, 8.0, 3.0, 6.0]
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")