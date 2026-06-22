def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_sequence_sum(data):
    try:
        validate_input(data)
        return sum(data)
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = [1, 5, 10, 20, 3]
    result = calculate_sequence_sum(sample_list)
    if result is not None:
        print(result)