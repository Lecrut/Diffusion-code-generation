def is_valid_letter(char):
    return 'a' <= char <= 'z'

def find_repeated_letters(text):
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if is_valid_letter(char):
            letter_counts[char] = letter_counts.get(char, 0) + 1
    repeated_letters = [letter for letter, count in letter_counts.items() if count >= 2]
    return sorted(repeated_letters)
if __name__ == '__main__':
    sample1 = 'Hello World'
    sample2 = 'Programming is fun'
    sample3 = 'Alphabet'
    sample4 = 'Mississippi'
    sample5 = 'aabbaa'
    print(find_repeated_letters(sample1))
    print(find_repeated_letters(sample2))
    print(find_repeated_letters(sample3))
    print(find_repeated_letters(sample4))
    print(find_repeated_letters(sample5))