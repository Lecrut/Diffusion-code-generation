import string
def find_repeated_letters(text):
    letter_counts = {}
    for char in text:
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
    sample_string_1 = "hello world"
    sample_string_2 = "programming is fun"
    sample_string_3 = "aabbccddeeff"
    sample_string_4 = "abcde"
    result_1 = find_repeated_letters(sample_string_1)
    result_2 = find_repeated_letters(sample_string_2)
    result_3 = find_repeated_letters(sample_string_3)
    result_4 = find_repeated_letters(sample_string_4)
    print(f"'{sample_string_1}': {result_1}")
    print(f"'{sample_string_2}': {result_2}")
    print(f"'{sample_string_3}': {result_3}")
    print(f"'{sample_string_4}': {result_4}")