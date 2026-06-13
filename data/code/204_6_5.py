import statistics
def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    elif n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 4.0]
    median_value = find_median(sample_list)
    print(median_value)
    sample_list_even = [1.0, 5.0, 2.0, 4.0]
    median_value_even = find_median(sample_list_even)
    print(median_value_even)
    sample_list_odd = [10.0, 20.0, 30.0, 40.0, 50.0]
    median_value_odd = find_median(sample_list_odd)
    print(median_value_odd)
    empty_list = []
    median_empty = find_median(empty_list)
    print(median_empty)