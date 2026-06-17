def find_print_index(numbers: list[int], target: int) -> tuple[bool, int]:
    try:
        for idx, num in enumerate(numbers):
            if num == target:
                return True, idx
        return False, -1
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        raise
if __name__ == '__main__':
    sample_list = [50, 23, 89, 45, 67]
    target_value = 89
    exists, index = find_print_index(sample_list, target_value)
    if exists:
        print(f"Target {target_value} found at index {index}")
    else:
        print(f"Target {target_value} not found in the list")