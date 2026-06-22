def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_numerical_minimum(data):
    validate_input(data)
    numerical_data = [x for x in data if isinstance(x, (int, float))]
    if not numerical_data:
        raise TypeError("No numerical data found in the list")
    minimum = min(numerical_data)
    return minimum

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, "a", 0]
    try:
        result = find_numerical_minimum(sample_list)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")