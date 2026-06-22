def validate_input(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    for item in sequence:
        if not isinstance(item, (int, float)):
            raise TypeError("All elements must be numbers")

def calculate_average(sequence):
    total_sum = sum(sequence)
    count = len(sequence)
    return total_sum / count

def average_of_sequence(sequence):
    validate_input(sequence)
    return calculate_average(sequence)

if __name__ == '__main__':
    sample_sequence = [1.5, 2.5, 3.5, 4.5]
    print(average_of_sequence(sample_sequence))