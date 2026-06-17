def calculate_print_index(target: int) -> int:
    if target <= 0:
        return -1
    sequence = [2**i for i in range(31)]
    try:
        idx = sequence.index(target)
        return idx + 1
    except ValueError:
        return None
if __name__ == '__main__':
    sample_targets = [4, 8, 16, 256]
    for target in sample_targets:
        index = calculate_print_index(target)
        if index is not None:
            print(f"Target {target}: Print Index {index}")
        else:
            print(f"Target {target}: Invalid Target")