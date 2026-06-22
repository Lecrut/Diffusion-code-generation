def validate_sequence(sequence):
    if not isinstance(sequence, str) or len(sequence) != 2:
        raise ValueError("Sequence must be a string of length 2")
    
def generate_extended_string(pattern, repetitions):
    return pattern * repetitions

if __name__ == '__main__':
    pattern = 'AB'
    repetitions = 1000
    validate_sequence(pattern)
    result = generate_extended_string(pattern, repetitions)
    print(result)