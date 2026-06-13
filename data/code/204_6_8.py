def find_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    sample_list2 = [10.0, 5.0, 2.0, 7.0, 1.0]
    sample_list3 = [1.0, 2.0, 3.0, 4.0]
    sample_list4 = [5.5, 1.5, 8.5, 2.5]
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")
    print(f"Median of {sample_list4}: {find_median(sample_list4)}")