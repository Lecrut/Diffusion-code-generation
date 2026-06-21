def validate_numbers(numbers):
    if not all(isinstance(num, float) for num in numbers):
        raise ValueError("All elements must be floating-point numbers")

def sort_descending(numbers):
    validate_numbers(numbers)
    numbers.sort(key=lambda x: -x)
    return numbers

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    sorted_values = sort_descending(sample_values)
    print(sorted_values)