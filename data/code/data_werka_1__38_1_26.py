def is_valid_letter(char):
    return 'a' <= char <= 'z'

def count_letters(text):
    letter_counts = {}
    for char in text:
        if is_valid_letter(char):
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def find_repeated_letters(s):
    letter_counts = count_letters(s)
    repeated_letters = set()
    for letter, count in letter_counts.items():
        if count > 1:
            repeated_letters.add(letter)
    return repeated_letters

if __name__ == '__main__':
    test_string_1 = "hello world"
    result_1 = find_repeated_letters(test_string_1)
    print(f"Input: '{test_string_1}', Repeated Letters: {result_1}")
    
    test_string_2 = "programming"
    result_2 = find_repeated_letters(test_string_2)
    print(f"Input: '{test_string_2}', Repeated Letters: {result_2}")
    
    test_string_3 = "abcde"
    result_3 = find_repeated_letters(test_string_3)
    print(f"Input: '{test_string_3}', Repeated Letters: {result_3}")