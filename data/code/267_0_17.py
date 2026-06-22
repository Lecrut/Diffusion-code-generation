def is_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return len(word) > 10

if __name__ == '__main__':
    sample_string_one = "short"
    sample_string_two = "thisisalongstring"
    sample_string_three = "tenchars"
    
    print(f"'{sample_string_one}' is long: {is_long(sample_string_one)}")
    print(f"'{sample_string_two}' is long: {is_long(sample_string_two)}")
    print(f"'{sample_string_three}' is long: {is_long(sample_string_three)}")