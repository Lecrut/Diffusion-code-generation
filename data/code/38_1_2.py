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
    sample_string1 = "hello world"
    sample_string2 = "programming"
    sample_string3 = "alphabet"
    sample_string4 = "aabbccddeeffg"
    result1 = find_repeated_letters(sample_string1)
    result2 = find_repeated_letters(sample_string2)
    result3 = find_repeated_letters(sample_string3)
    result4 = find_repeated_letters(sample_string4)
    print(f"'{sample_string1}': {result1}")
    print(f"'{sample_string2}': {result2}")
    print(f"'{sample_string3}': {result3}")
    print(f"'{sample_string4}': {result4}")