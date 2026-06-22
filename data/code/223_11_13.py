def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("All elements must be numbers")

def find_max_element(numbers):
    max_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    validate_input(sample_values)
    result = find_max_element(sample_values)
    print(result)