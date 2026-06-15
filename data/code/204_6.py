import statistics
def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list1 = [3.5, 1.0, 4.5, 2.0, 3.0]
    sample_list2 = [10.5, 5.0, 15.5, 2.5, 8.0, 1.0]
    sample_list3 = [7.0, 2.0, 4.0, 1.0, 5.0, 3.0]
    sample_list4 = [1.1, 2.2, 3.3, 4.4]
    sample_list5 = []
    print(f"Median of {sample_list1}: {find_median(sample_list1)}")
    print(f"Median of {sample_list2}: {find_median(sample_list2)}")
    print(f"Median of {sample_list3}: {find_median(sample_list3)}")
    print(f"Median of {sample_list4}: {find_median(sample_list4)}")
    try:
        find_median(sample_list5)
    except ValueError as e:
        print(f"Error for {sample_list5}: {e}")