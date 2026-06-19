def find_repeated_letters(input_string):
    letter_count = {}
    repeated_letters = set()
    
    for char in input_string:
        if 'a' <= char.lower() <= 'z':
            if char in letter_count:
                letter_count[char] += 1
                repeated_letters.add(char)
            else:
                letter_count[char] = 1
    
    return sorted(list(repeated_letters))

if __name__ == '__main__':
    sample_string_1 = "programming"
    sample_string_2 = "hello world"
    sample_string_3 = "abcdefg"
    sample_string_4 = "aabbccddeeff"
    
    print(f"Input: {sample_string_1}")
    print("Repeated letters found:", find_repeated_letters(sample_string_1))
    
    print(f"Input: {sample_string_2}")
    print("Repeated letters found:", find_repeated_letters(sample_string_2))
    
    print(f"Input: {sample_string_3}")
    print("Repeated letters found:", find_repeated_letters(sample_string_3))
    
    print(f"Input: {sample_string_4}")
    print("Repeated letters found:", find_repeated_letters(sample_string_4))