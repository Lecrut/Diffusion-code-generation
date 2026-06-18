def calculate_print_index(target: int) -> str:
    if target < 0:
        return "Index out of range"
    indices = ["Zero", "One", "Two", "Three", "Four"]
    try:
        idx = int(target)
        for i, label in enumerate(indices):
            if idx == i:
                return f"{label} ({i})"
        remaining_indices = len(indices) - 1
        if idx > len(indices) - 1:
            return f"Index {idx}"
    except ValueError:
        return "Invalid input type"
if __name__ == '__main__':
    sample_targets = [0, 3, 5]
    for target in sample_targets:
        result = calculate_print_index(target)
        print(result)