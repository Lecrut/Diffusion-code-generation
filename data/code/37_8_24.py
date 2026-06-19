def is_valid_string(s):
    return isinstance(s, str)

def combine_strings(str1, str2):
    if not is_valid_string(str1) or not is_valid_string(str2):
        raise ValueError("Both arguments must be strings")
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    result1 = combine_strings(string_a, string_b)
    print(result1)
    
    string_c = "Python"
    string_d = "Programming"
    result2 = combine_strings(string_d, string_c)
    print(result2)