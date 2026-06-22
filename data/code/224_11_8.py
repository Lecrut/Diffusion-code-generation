def validate_sequence(sequence):
    if not all(isinstance(x, int) for x in sequence):
        raise ValueError("All elements in the sequence must be integers.")
    if len(sequence) == 0:
        raise ValueError("The sequence cannot be empty.")

def calculate_average(sequence):
    validate_sequence(sequence)
    total = sum(sequence)
    count = len(sequence)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    avg = calculate_average(sample_values)
    print(avg)