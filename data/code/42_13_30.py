def concatenate_strings(string_list):
    if not string_list:
        return ""
    if not all(isinstance(s, str) for s in string_list):
        raise TypeError("All elements must be strings")
    return ''.join(string_list)

if __name__ == '__main__':
    SAMPLE_VALUES = ["apple", "banana", "cherry", "date"]
    try:
        result = concatenate_strings(SAMPLE_VALUES)
        print(result)
    except TypeError as e:
        print(e)