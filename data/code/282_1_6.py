def validate_input(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements in the sequence must be integers")

def calculate_sequence_sum(data):
    validate_input(data)
    return sum(data)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(sample_list)
    print(result)