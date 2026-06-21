def print_characters_by_indices(s, indices):
    if not isinstance(s, str):
        raise ValueError('The first argument must be a string.')
    if not all((isinstance(i, int) for i in indices)):
        raise ValueError('All elements in the second argument must be integers.')
    valid_indices = [i for i in indices if 0 <= i < len(s)]
    result = ''.join((s[i] for i in valid_indices))
    return result
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    sample_indices = [0, 7, 8, 12, 15]
    print(print_characters_by_indices(sample_string, sample_indices))