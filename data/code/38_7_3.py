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
    sample1 = "Hello World"
    sample2 = "Programming is fun"
    sample3 = "AaBbCc"
    sample4 = "Indivisibilities"
    sample5 = "Alphabet"
    print(f"'{sample1}': {find_repeated_letters(sample1)}")
    print(f"'{sample2}': {find_repeated_letters(sample2)}")
    print(f"'{sample3}': {find_repeated_letters(sample3)}")
    print(f"'{sample4}': {find_repeated_letters(sample4)}")
    print(f"'{sample5}': {find_repeated_letters(sample5)}")