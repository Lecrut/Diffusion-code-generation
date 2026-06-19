def is_valid_string(s):
    return isinstance(s, str)

def combine_strings(str1, str2):
    if not is_valid_string(str1) or not is_valid_string(str2):
        raise ValueError("Both arguments must be strings")
    return str1 + str2

if __name__ == '__main__':
    first_string = "Hello"
    second_string = " World"
    result = combine_strings(first_string, second_string)
    print(result)