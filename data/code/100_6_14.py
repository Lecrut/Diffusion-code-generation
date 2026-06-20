def is_valid_and_operation(sequence):
    return all(char == '1' for char in sequence)

if __name__ == '__main__':
    test_sequence = '1110'
    print(is_valid_and_operation(test_sequence))