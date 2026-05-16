import string
def find_repeated_letters(text):
    letter_counts = {}
    for char in text:
        if 'a' <= char <= 'z':
            letter = char.lower()
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    repeated_letters = set()
    for letter, count in letter_counts.items():
        if count > 1:
            repeated_letters.add(letter)
    return repeated_letters
if __name__ == '__main__':
    sample_string_1 = "hello world"
    sample_string_2 = "programming"
    sample_string_3 = "alphabet"
    sample_string_4 = "unique"
    sample_string_5 = "aabbccddeeff"
    sample_string_6 = "Mississippi"
    result_1 = find_repeated_letters(sample_string_1)
    result_2 = find_repeated_letters(sample_string_2)
    result_3 = find_repeated_letters(sample_string_3)
    result_4 = find_repeated_letters(sample_string_4)
    result_5 = find_repeated_letters(sample_string_5)
    result_6 = find_repeated_letters(sample_string_6)
    print(f"'{sample_string_1}': {result_1}")
    print(f"'{sample_string_2}': {result_2}")
    print(f"'{sample_string_3}': {result_3}")
    print(f"'{sample_string_4}': {result_4}")
    print(f"'{sample_string_5}': {result_5}")
    print(f"'{sample_string_6}': {result_6}")