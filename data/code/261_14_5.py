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
    list1 = [3.5, 1.0, 4.5, 2.0]
    list2 = [7.0, 1.0, 9.0, 3.0, 5.0]
    list3 = [10.0]
    list4 = []
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    try:
        calculate_median(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")