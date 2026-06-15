def find_median(data):
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
    sample_list1 = [1.5, 3.1, 2.8, 4.0, 1.9]
    sample_list2 = [10.5, 5.2, 8.1, 3.3, 6.7]
    sample_list3 = [1.0, 2.0, 3.0, 4.0]
    sample_list4 = [7.0]
    sample_list5 = []
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")
    print(f"Median of {sample_list4}: {find_median(sample_list4)}")
    print(f"Median of {sample_list5}: {find_median(sample_list5)}")