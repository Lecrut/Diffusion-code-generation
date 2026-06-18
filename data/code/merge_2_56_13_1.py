def calculate_print_index(target: int) -> str:
    if 1 <= target <= 5:
        return f"Print Index {target}"
    raise ValueError("Target must be between 1 and 5.")
if __name__ == '__main__':
    sample_targets = [3, -2, 7]
    for target in sample_targets:
        try:
            result = calculate_print_index(target)
            print(result)
        except ValueError as error:
            print(f"Error processing {target}: {error}")