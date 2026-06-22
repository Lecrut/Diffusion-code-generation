def calculate_average(sequence):
    return sum(sequence) / len(sequence)

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    print(calculate_average(sample_sequence))