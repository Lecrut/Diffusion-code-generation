def combine_strings(str1, str2):
    def validate_input(s1, s2):
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise ValueError("Both inputs must be strings")
    
    validate_input(str1, str2)
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    result1 = combine_strings(string_a, string_b)
    print(result1)
    
    string_c = "Python"
    string_d = "Programming"
    result2 = combine_strings(string_c, string_d)
    print(result2)