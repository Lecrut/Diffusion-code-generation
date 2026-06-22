def validate_data(data):
    if not isinstance(data, list) or not all(isinstance(pair, tuple) for pair in data):
        raise ValueError("Input must be a list of tuples")
    if any(len(pair) == 0 for pair in data):
        raise ValueError("Tuples cannot be empty")

def calculate_average_of_pairs(data):
    validate_data(data)
    total_sum = sum(sum(pair) for pair in data)
    total_count = sum(len(pair) for pair in data)
    return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4, 5),
        (6, 7)
    ]
    average = calculate_average_of_pairs(sample_data)
    print(average)