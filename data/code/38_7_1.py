import string
def find_repeated_letters(text):
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    repeated_letters = set()
    for letter, count in letter_counts.items():
        if count >= 2:
            repeated_letters.add(letter)
    return sorted(list(repeated_letters))
if __name__ == '__main__':
    sample_string1 = "Hello World"
    sample_string2 = "Programming is fun"
    sample_string3 = "aabbccddeeffgghh"
    sample_string4 = "Alphabet"
    sample_string5 = "Mississippi"
    result1 = find_repeated_letters(sample_string1)
    result2 = find_repeated_letters(sample_string2)
    result3 = find_repeated_letters(sample_string3)
    result4 = find_repeated_letters(sample_string4)
    result5 = find_repeated_letters(sample_string5)
    print(f"'{sample_string1}': {result1}")
    print(f"'{sample_string2}': {result2}")
    print(f"'{sample_string3}': {result3}")
    print(f"'{sample_string4}': {result4}")
    print(f"'{sample_string5}': {result5}")