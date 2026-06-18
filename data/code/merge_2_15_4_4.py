def sort_numbers(numbers: list[float], stable: bool = True) -> list[float]:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric, got {type(item).__name__}.")
    return sorted(numbers, key=lambda x: -x)
if __name__ == '__main__':
    sample_data = [3.5, 1.2, 4.8, 2.0, 3.9]
    result_stable = sort_numbers(sample_data.copy(), stable=True)
    result_unstable = sort_numbers(sample_data.copy(), stable=False)
    print("Original:", sample_data)
    print("Sorted (Stable):", result_stable)
    print("Sorted (Unstable):", result_unstable)