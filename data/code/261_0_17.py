def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 1:
        median = sorted_data[mid_index]
    else:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
    return median

if __name__ == '__main__':
    sample_list_odd = [5, 2, 8, 1, 9]
    sample_list_even = [10, 4, 7, 3, 1]
    try:
        median_odd = calculate_median(sample_list_odd)
        print("Median of odd list:", median_odd)
        median_even = calculate_median(sample_list_even)
        print("Median of even list:", median_even)
    except ValueError as e:
        print(e)