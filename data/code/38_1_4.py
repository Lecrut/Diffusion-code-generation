def find_repeated_letters(s):
    letter_counts = {}
    for char in s:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    repeated_letters = set()
    for letter, count in letter_counts.items():
        if count > 1:
            repeated_letters.add(letter)
    return repeated_letters
if __name__ == '__main__':
    test_string1 = "hello world"
    result1 = find_repeated_letters(test_string1)
    print(f"Input: '{test_string1}', Repeated Letters: {result1}")
    test_string2 = "programming"
    result2 = find_repeated_letters(test_string2)
    print(f"Input: '{test_string2}', Repeated Letters: {result2}")
    test_string3 = "abcde"
    result3 = find_repeated_letters(test_string3)
    print(f"Input: '{test_string3}', Repeated Letters: {result3}")
    test_string4 = "aabbccddeeff"
    result4 = find_repeated_letters(test_string4)
    print(f"Input: '{test_string4}', Repeated Letters: {result4}")