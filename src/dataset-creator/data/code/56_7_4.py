def compute_print_index(target: int) -> int:
    if target <= 0:
        return -1
    sequence = [i * i + 2 * i + 3 for i in range(5)]
    for idx, val in enumerate(sequence):
        if val == target:
            return idx
    return len(sequence)
if __name__ == '__main__':
    sample_target = 10
    result_index = compute_print_index(sample_target)
    print(result_index)