def validate_numeric_list(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numeric")

def find_smallest_value(numbers):
    validate_numeric_list(numbers)
    return min(numbers)

if __name__ == '__main__':
    sample_values = [-5, 3, -1, 2, -4]
    print(find_smallest_value(sample_values))