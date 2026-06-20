def and_checker(sequence):
    return all(bit == '1' for bit in sequence)

if __name__ == '__main__':
    test_cases = [
        ('111', True),
        ('011', False),
        ('101', False),
        ('110', False),
        ('000', False),
        ('111111', True)
    ]
    for seq, expected in test_cases:
        result = and_checker(seq)
        print(f"Sequence: {seq}, Expected: {expected}, Result: {result}")