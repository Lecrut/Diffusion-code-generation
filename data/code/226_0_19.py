numbers = [1, 2, 3, 4, 5]

def validate_sequence(sequence):
    if not isinstance(sequence, list) or not all(isinstance(x, int) for x in sequence):
        raise ValueError("Sequence must be a list of integers")

def repeat_elements(sequence, repetitions):
    validate_sequence(sequence)
    result = []
    for element in sequence:
        result.extend([element] * repetitions)
    return result

if __name__ == '__main__':
    repeated_sequence = repeat_elements(numbers, 10)
    print(repeated_sequence)