def is_valid_and(sequence):
    return all(char == '1' for char in sequence)

if __name__ == '__main__':
    sample_sequence = '1101'
    print(is_valid_and(sample_sequence))