def is_valid_and_operation(sequence):
    return all(char == '1' for char in sequence)

if __name__ == '__main__':
    test_cases = [
        ('111', True),
        ('000', False),
        ('101', False),
        ('110', False)
    ]
    results = {sequence: is_valid_and_operation(sequence) for sequence, _ in test_cases}
    print(results)