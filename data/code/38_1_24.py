def find_repeated_letters(s):
    letter_counts = {}
    for char in s:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return {letter for letter, count in letter_counts.items() if count > 1}

if __name__ == '__main__':
    test_string_1 = "hello world"
    result_1 = find_repeated_letters(test_string_1)
    print(f"Input: '{test_string_1}', Repeated Letters: {result_1}")
    
    test_string_2 = "programming"
    result_2 = find_repeated_letters(test_string_2)
    print(f"Input: '{test_string_2}', Repeated Letters: {result_2}")
    
    test_string_3 = "abcdefg"
    result_3 = find_repeated_letters(test_string_3)
    print(f"Input: '{test_string_3}', Repeated Letters: {result_3}")