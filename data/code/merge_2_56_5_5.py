import sys
def calculate_print_index(target: int) -> int:
    if target <= 0:
        raise ValueError("Target must be positive.")
    return (target - 1) // 25 + 1
if __name__ == '__main__':
    sample_targets = [1, 76, 100]
    for t in sample_targets:
        index = calculate_print_index(t)
        print(f"Target {t}: Print Index {index}")