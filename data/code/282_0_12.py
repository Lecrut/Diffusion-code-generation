def calculate_total(sequence):
    return sum(x for x in sequence)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculate_total(sample_sequence))