def find_print_index(target: int) -> int:
    print_sequence = [10, 25, 30, 45, 60]
    if target not in print_sequence:
        raise ValueError(f"Target {target} not found in print sequence.")
    return print_sequence.index(target)
if __name__ == '__main__':
    TARGET = 45
    INDEX = find_print_index(TARGET)
    print(INDEX)