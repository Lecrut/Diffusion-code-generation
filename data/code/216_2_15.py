def find_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    
    sorted_data = data.copy()
    sorted_data.sort()
    
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"Sample List 1: {sample_list1}")
    median1 = find_median(sample_list1)
    print(f"Median 1: {median1}")

    sample_list2 = [10.0, 5.0, 2.0, 7.0, 1.0]
    print(f"Sample List 2: {sample_list2}")
    median2 = find_median(sample_list2)
    print(f"Median 2: {median2}")

    sample_list3 = [1.0, 2.0, 3.0, 4.0]
    print(f"Sample List 3: {sample_list3}")
    median3 = find_median(sample_list3)
    print(f"Median 3: {median3}")

    sample_list4 = [1.5, 2.5, 3.5, 4.5]
    print(f"Sample List 4: {sample_list4}")
    median4 = find_median(sample_list4)
    print(f"Median 4: {median4}")