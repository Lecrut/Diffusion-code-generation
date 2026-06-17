def compute_print_index(target: int) -> int:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be an integer.")
    return abs(int(target)) % 10
if __name__ == '__main__':
    sample_target = 42.789
    result_index = compute_print_index(sample_target)
    print(f"Print index for target {sample_target}: {result_index}")