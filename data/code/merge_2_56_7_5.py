def compute_print_index(target: int) -> int:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be numeric.")
    return abs(int(target)) % 10
if __name__ == '__main__':
    sample_target = 34.7
    result_index = compute_print_index(sample_target)
    print(result_index)