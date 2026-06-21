def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be integers or floats.")

def sort_by_descending(numbers):
    validate_input(numbers)
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [12, 45, 67, 89, 34, 23]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)