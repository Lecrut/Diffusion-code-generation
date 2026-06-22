def find_repeated_letters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    seen = set()
    repeated = set()
    
    for char in input_string:
        lower_char = char.lower()
        if 'a' <= lower_char <= 'z':
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    
    return repeated

if __name__ == '__main__':
    sample_string = "alibaba cloud"
    result = find_repeated_letters(sample_string)
    print("Repeated letters:", result)
    
    sample_string_2 = "hello world"
    result_2 = find_repeated_letters(sample_string_2)
    print("Repeated letters:", result_2)