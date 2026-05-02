import string
def find_repeated_letters(s):
    letter_counts = {}
    for char in s:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
        elif 'A' <= char <= 'Z':
            letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1
    repeated_letters = set()
    for letter, count in letter_counts.items():
        if count > 1:
            repeated_letters.add(letter)
    return repeated_letters
if __name__ == '__main__':
    test_string_1 = "hello world"
    test_string_2 = "programming"
    test_string_3 = "alphabet"
    test_string_4 = "aabbccddeeff"
    test_string_5 = "unique"
    result_1 = find_repeated_letters(test_string_1)
    result_2 = find_repeated_letters(test_string_2)
    result_3 = find_repeated_letters(test_string_3)
    result_4 = find_repeated_letters(test_string_4)
    result_5 = find_repeated_letters(test_string_5)
    print(f"'{test_string_1}': {result_1}")
    print(f"'{test_string_2}': {result_2}")
    print(f"'{test_string_3}': {result_3}")
    print(f"'{test_string_4}': {result_4}")
    print(f"'{test_string_5}': {result_5}")