def is_valid_list(numbers):
    for element in numbers:
        if not isinstance(element, (int, float)):
            raise ValueError("All elements must be numeric")
    return True

def calculate_list_sum(numbers):
    if not is_valid_list(numbers):
        raise ValueError("Invalid list provided")
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(calculate_list_sum(sample_values))
    sample_values = [10.5, 20.5, 30.0]
    print(calculate_list_sum(sample_values))
    sample_values = [-1, 5, -3, 10]
    print(calculate_list_sum(sample_values))