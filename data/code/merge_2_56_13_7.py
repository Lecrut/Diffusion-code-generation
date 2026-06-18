def get_print_index(target: int) -> int:
    return abs(target % 10)
if __name__ == '__main__':
    sample_targets = [3, -7, 24]
    for target in sample_targets:
        idx = get_print_index(target)
        print(f"Target {target} -> Print Index {idx}")