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
    sample1 = "hello world"
    sample2 = "programming"
    sample3 = "aabbccddeeff"
    sample4 = "abcde"
    sample5 = "Mississippi"
    print(f"'{sample1}': {find_repeated_letters(sample1)}")
    print(f"'{sample2}': {find_repeated_letters(sample2)}")
    print(f"'{sample3}': {find_repeated_letters(sample3)}")
    print(f"'{sample4}': {find_repeated_letters(sample4)}")
    print(f"'{sample5}': {find_repeated_letters(sample5)}")