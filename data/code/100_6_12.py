def is_valid_and(sequence):
    return all(char == '1' for char in sequence)

if __name__ == '__main__':
    print(is_valid_and('111'))
    print(is_valid_and('011'))
    print(is_valid_and('101'))
    print(is_valid_and('110'))