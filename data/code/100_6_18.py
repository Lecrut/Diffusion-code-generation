def validate_and_sequence(sequence):
    if not sequence:
        raise ValueError('Sequence cannot be empty')
    if any((char not in '01' for char in sequence)):
        raise ValueError("Sequence must contain only '0's and '1's")
    return all((char == '1' for char in sequence))
if __name__ == '__main__':
    print(validate_and_sequence('111'))
    print(validate_and_sequence('010'))
    print(validate_and_sequence('101'))
    print(validate_and_sequence('110'))
    print(validate_and_sequence(''))
    print(validate_and_sequence('123'))