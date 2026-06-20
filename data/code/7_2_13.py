def contains_special_characters(input_string):
    special_symbols = set("!@#$%^&*()-_=+[]{}|;:,.<>?/~`")
    input_chars = set(input_string)
    return len(input_chars.intersection(special_symbols)) > 0

if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Hello@World!"
    
    result_1 = contains_special_characters(test_string_1)
    result_2 = contains_special_characters(test_string_2)
    
    print(result_1)
    print(result_2)