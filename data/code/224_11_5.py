def validate_sequence(sequence):
    if not sequence:
        return False
    for item in sequence:
        if not isinstance(item, int):
            return False
    return True

def calculate_average(sequence):
    if not validate_sequence(sequence):
        raise ValueError("Invalid sequence")
    return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    average = calculate_average(sample_sequence)
    print(average)