def concatenate_strings(string_list):
    if not all(isinstance(item, str) for item in string_list):
        raise TypeError("All elements must be strings")
    return ''.join(string_list)

if __name__ == '__main__':
    sample_values = ["Hello", " ", "World", "!"]
    result = concatenate_strings(sample_values)
    print(result)