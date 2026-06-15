def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    return median
if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [4, 1, 5, 2, 3]
    list3 = [10, 20, 30, 40]
    list4 = []
    list5 = [7]
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    try:
        print(f"Median of {list4}: {calculate_median(list4)}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")
    print(f"Median of {list5}: {calculate_median(list5)}")