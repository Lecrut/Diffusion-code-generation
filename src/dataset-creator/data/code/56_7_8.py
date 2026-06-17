def compute_print_index(target: int) -> int:
    left = 0
    right = len([i for i in range(1_000_000)]) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return mid
        elif mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
if __name__ == '__main__':
    sample_target = 50_000
    result_index = compute_print_index(sample_target)
    print(f"Target {sample_target} found at index: {result_index}")