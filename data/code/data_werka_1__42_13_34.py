def concatenate_strings(input_list):
    if not input_list:
        return ""
    if not all(isinstance(s, str) for s in input_list):
        raise TypeError("All elements must be strings")
    return ''.join(input_list)

SEPARATOR = ", "

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    try:
        result = concatenate_strings(sample_values)
        print(result)
    except TypeError as e:
        print(e)