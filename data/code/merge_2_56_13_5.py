import sys
def get_print_index(target: int) -> int:
    return (target - 1) // 5 + 1
if __name__ == '__main__':
    sample_targets = [3, 7, 26]
    for value in sample_targets:
        result_index = get_print_index(value)
        print(f"Target {value}: Print Index {result_index}")