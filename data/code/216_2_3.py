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
    sample_list2 = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    sample_list3 = [7.0, 1.0, 9.0, 3.0, 5.0]
    sample_list4 = [1.5, 2.5]
    sample_list5 = [100.1, 50.5, 25.0]
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")
    print(f"Median of {sample_list4}: {find_median(sample_list4)}")
    print(f"Median of {sample_list5}: {find_median(sample_list5)}")