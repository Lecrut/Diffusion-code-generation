import sys
def find_print_index(numbers: list[int], target: int) -> int | None:
    for idx, num in enumerate(numbers):
        if num == target:
            return idx
    return None
if __name__ == '__main__':
    sample_numbers = [10, 25, 30, 40, 50]
    target_value = 30
    index = find_print_index(sample_numbers, target_value)
    if index is not None:
        print(f"Target {target_value} found at index {index}.")
    else:
        print("Target value not found in the list.")