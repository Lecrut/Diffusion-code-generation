import timeit
def find_print_index(data: list[int], target: int) -> int | None:
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
def generate_sample_data(size: int, min_val: int, max_val: int) -> list[int]:
    data = []
    for i in range(min_val, max_val + 1):
        if len(data) < size or (i - min_val) % ((max_val - min_val) // size * 2) == 0:
            data.append(i)
    return sorted(list(set(data)))
if __name__ == '__main__':
    sample_data = generate_sample_data(100, 1, 500)
    target_value = 347
    result_index = find_print_index(sample_data, target_value)
    print(f"Target: {target_value}")
    print(f"Found at index: {result_index}" if result_index is not None else "Not found")