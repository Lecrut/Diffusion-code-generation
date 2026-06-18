import statistics as stats
def find_center_mark(arr):
    if not arr:
        raise ValueError("Input array cannot be empty.")
    try:
        sorted_arr = sorted(arr)
        n = len(sorted_arr)
        mid_idx = n // 2
        if n % 2 == 0:
            return (sorted_arr[mid_idx - 1] + sorted_arr[mid_idx]) / 2.0
        else:
            return int(sorted_arr[mid_idx])
    except Exception as e:
        raise RuntimeError(f"Error processing array center mark calculation") from e
if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 2]
    result = find_center_mark(sample_data)
    print(result)