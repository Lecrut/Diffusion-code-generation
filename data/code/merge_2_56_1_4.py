import sys
def find_print_index(numbers: list[int], target: int) -> int | None:
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return None
if __name__ == '__main__':
    sample_numbers = [10, 25, 30, 45, 25, 60]
    hard_target = 30
    try:
        index_result = find_print_index(sample_numbers, hard_target)
        if index_result is not None:
            print(f"The target number {hard_target} was found at index {index_result}.")
        else:
            raise ValueError(f"Target value '{hard_target}' does not exist in the list.")
    except (ValueError, TypeError) as error:
        print(f"An unexpected error occurred during processing: {error}", file=sys.stderr)