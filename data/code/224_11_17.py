def validate_sequence(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    for num in sequence:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    validate_sequence(sample_sequence)
    avg = calculate_average(sample_sequence)
    print(avg)