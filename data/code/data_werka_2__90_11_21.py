def contains_leading_a_or_b(input_sequence):
    if not isinstance(input_sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple of strings")
    for item in input_sequence:
        if not isinstance(item, str):
            raise TypeError("All items must be strings")
        if len(item) == 0:
            continue
        first_char = item[0]
        if first_char == 'A' or first_char == 'B':
            return True
    return False

if __name__ == '__main__':
    test_list = ['Apple', 'Banana', 'Cherry']
    print(contains_leading_a_or_b(test_list))
    test_list_2 = ['Dog', 'Elephant', 'Cat']
    print(contains_leading_a_or_b(test_list_2))