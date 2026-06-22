def validate_sequence(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

def calculate_sequence_sum(data):
    validate_sequence(data)
    return sum(data)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 20, 3]
    result = calculate_sequence_sum(sample_list)
    print(result)