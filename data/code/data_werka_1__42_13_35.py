def concatenate_strings(string_list):
    if not all(isinstance(s, str) for s in string_list):
        raise TypeError("All elements must be strings")
    return ''.join(string_list)

if __name__ == '__main__':
    sample_values = ["Hello", "World", "!"]
    try:
        result = concatenate_strings(sample_values)
        print(result)
    except TypeError as e:
        print(e)