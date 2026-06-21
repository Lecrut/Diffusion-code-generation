def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def find_absolute_minimum(data):
    validate_input(data)
    return sorted(data)[0]

if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -10.0, 0.5, 42.0]
    try:
        result = find_absolute_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")