def average(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    if not all(isinstance(x, (int, float)) for x in sequence):
        raise TypeError("All elements must be numbers")
    return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(average(sample_sequence))