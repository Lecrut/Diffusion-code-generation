def find_smallest_string(strings):
    try:
        if strings and all((isinstance(s, str) for s in strings)):
            return min(strings)
        else:
            raise ValueError('Input list must contain only non-empty strings.')
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry']
    result = find_smallest_string(sample_strings)
    print(result)