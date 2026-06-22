def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")

def find_largest(data):
    if not data:
        return None
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 22, 4, 30, 11]
    validate_input(sample_list)
    result = find_largest(sample_list)
    print(result)