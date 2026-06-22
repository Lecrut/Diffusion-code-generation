def calculate_sequence_sum(data):
    if not all(isinstance(x, int) for x in data):
        raise ValueError("All elements in the sequence must be integers.")
    return sum(data)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    try:
        result = calculate_sequence_sum(sample_sequence)
        print(result)
    except ValueError as e:
        print(e)