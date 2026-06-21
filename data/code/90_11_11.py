def starts_with_a_or_b(strings):
    if not isinstance(strings, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    def is_valid_target(first_char):
        valid_chars = {'A', 'B'}
        return first_char in valid_chars

    def has_valid_prefix(s):
        if len(s) == 0:
            return False
        return is_valid_target(s[0])

    for s in strings:
        if not isinstance(s, str):
            continue
        if has_valid_prefix(s):
            return True
    return False

if __name__ == '__main__':
    sample_list = ['Zebra', 'Bike', 'Car']
    result = starts_with_a_or_b(sample_list)
    print(result)
    sample_list_2 = ['Apple', 'Orange', 'Banana']
    result_2 = starts_with_a_or_b(sample_list_2)
    print(result_2)