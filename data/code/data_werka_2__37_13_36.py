def merge_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return ''.join([str1, str2])

if __name__ == '__main__':
    STRING_A = "Hello"
    STRING_B = "World"
    result = merge_strings(STRING_A, STRING_B)
    print(result)