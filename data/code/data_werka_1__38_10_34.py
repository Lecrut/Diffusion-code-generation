def find_repeated_letters(input_string):
    seen_letters = set()
    repeated_letters = set()
    
    for char in input_string:
        if 'a' <= char.lower() <= 'z':
            lower_char = char.lower()
            if lower_char in seen_letters:
                repeated_letters.add(lower_char)
            else:
                seen_letters.add(lower_char)
    
    return repeated_letters

if __name__ == '__main__':
    SAMPLE_STRING_1 = "programming"
    SAMPLE_STRING_2 = "hello world"
    SAMPLE_STRING_3 = "data analysis"

    result_1 = find_repeated_letters(SAMPLE_STRING_1)
    print("Repeated letters in", SAMPLE_STRING_1, ":", result_1)

    result_2 = find_repeated_letters(SAMPLE_STRING_2)
    print("Repeated letters in", SAMPLE_STRING_2, ":", result_2)

    result_3 = find_repeated_letters(SAMPLE_STRING_3)
    print("Repeated letters in", SAMPLE_STRING_3, ":", result_3)