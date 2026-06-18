def compute_print_index(target: int) -> int:
    if target < 0:
        raise ValueError("Target value must be non-negative.")
    index = 1
    current_sum = 0
    while True:
        next_value = index * (index + 1) // 2
        if next_value == target:
            return index - 1
        elif next_value > target:
            break
        current_sum += next_value
        index += 1
if __name__ == '__main__':
    sample_target = 55
    try:
        result_index = compute_print_index(sample_target)
        print(f"Print index for {sample_target} is {result_index}")
    except ValueError as e:
        print(f"Error: {e}")