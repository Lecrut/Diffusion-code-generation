def concatenate_strings(strings):
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    return ''.join(strings)

if __name__ == '__main__':
    sample_values = ["Hello", " ", "World", "!"]
    try:
        result = concatenate_strings(sample_values)
        print(result)
    except TypeError as e:
        print(e)