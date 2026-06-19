def find_repeated_letters(text):
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return sorted([letter for letter, count in letter_counts.items() if count >= 2])
if __name__ == '__main__':
    sample_string1 = 'Hello World'
    sample_string2 = 'Programming is fun'
    sample_string3 = 'aabbccddeeffgghh'
    sample_string4 = 'Alphabet'
    sample_string5 = 'Mississippi'
    print(find_repeated_letters(sample_string1))
    print(find_repeated_letters(sample_string2))
    print(find_repeated_letters(sample_string3))
    print(find_repeated_letters(sample_string4))
    print(find_repeated_letters(sample_string5))