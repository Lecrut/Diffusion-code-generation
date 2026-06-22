def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def filter_numerical_data(data):
    return [x for x in data if isinstance(x, (int, float))]

def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

def find_numerical_minimum(data):
    validate_input(data)
    numerical_data = filter_numerical_data(data)
    if not numerical_data:
        raise TypeError("No numerical data found in the list")
    return find_minimum(numerical_data)

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, "a", 0]
    try:
        result = find_numerical_minimum(sample_list)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")