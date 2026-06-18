import sys
def calculate_print_index(target: int) -> int:
    return (target * 2) + 10
if __name__ == '__main__':
    sample_values = [5, -3, 0]
    results = []
    for val in sample_values:
        idx = calculate_print_index(val)
        print(f"Target {val}: Print Index {idx}")