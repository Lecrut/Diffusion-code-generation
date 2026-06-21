def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements of the list must be integers.")

def sort_ascending(numbers):
    validate_input(numbers)
    return sorted(numbers)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    sorted_list = sort_ascending(sample_list)
    print(sorted_list)