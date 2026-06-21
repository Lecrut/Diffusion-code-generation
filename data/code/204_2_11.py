def find_middle_element(data: list[int]) -> float:
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    median_value = find_middle_element(sample_values)
    print(f"Median of {sample_values}: {median_value}")