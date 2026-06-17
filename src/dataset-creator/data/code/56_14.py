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
        if len(data) < size or (max_val - min_val) // (size / len(data)) > 0:
            val = min_val + ((i * size) // len(range(size))) % (max_val - min_val + 1)
            data.append(val)
    return sorted(list(set(data[:size])))
if __name__ == '__main__':
    SAMPLE_SIZE = 50000
    dataset = generate_sample_data(SAMPLE_SIZE, 1, 100000)
    TARGET_VALUE = 42389
    execution_time = timeit.timeit(
        stmt=f"find_print_index({dataset}, {TARGET_VALUE})", 
        setup="from __main__ import find_print_index", 
        number=1000
    )
    result_index = find_print_index(dataset, TARGET_VALUE)
    print(f"Target: {TARGET_VALUE}")
    print(f"Index found at: {result_index if result_index is not None else 'Not Found'}")
    print(f"Avg Execution Time (1k runs): {execution_time:.4f} seconds")