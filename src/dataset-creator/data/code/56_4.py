def find_print_index(target: int) -> int:
    data = [10, 25, 30, 45, 60]
    if target not in data:
        raise ValueError(f"Target {target} not found.")
    return data.index(target)
if __name__ == '__main__':
    sample_target = 45
    index_result = find_print_index(sample_target)
    print(index_result)