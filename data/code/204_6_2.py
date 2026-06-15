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
    sample_list_odd = [3.5, 1.0, 4.5, 2.0, 1.5]
    sample_list_even = [10.0, 20.0, 30.0, 40.0]
    sample_list_single = [99.9]
    sample_list_empty = []
    print(f"Median of {sample_list_odd}: {find_median(sample_list_odd)}")
    print(f"Median of {sample_list_even}: {find_median(sample_list_even)}")
    print(f"Median of {sample_list_single}: {find_median(sample_list_single)}")
    try:
        find_median(sample_list_empty)
    except ValueError as e:
        print(f"Error for empty list: {e}")