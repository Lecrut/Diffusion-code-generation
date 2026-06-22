def validate_input(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

def find_largest_element(numbers):
    validate_input(numbers)
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    print(find_largest_element(sample_values))