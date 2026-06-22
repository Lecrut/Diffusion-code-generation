def find_repeated_letters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    seen = set()
    repeated = set()
    
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    
    return repeated

if __name__ == '__main__':
    sample_string_1 = "Hello, World!"
    result_1 = find_repeated_letters(sample_string_1)
    print("Repeated letters in", sample_string_1, ":", result_1)
    
    sample_string_2 = "Programming is fun!"
    result_2 = find_repeated_letters(sample_string_2)
    print("Repeated letters in", sample_string_2, ":", result_2)