def find_repeated_letters(text):
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    repeated_letters = [letter for letter, count in letter_counts.items() if count >= 2]
    return sorted(repeated_letters)
if __name__ == '__main__':
    sample_text1 = 'Hello World'
    sample_text2 = 'Programming is fun'
    sample_text3 = 'Alibaba Cloud'
    sample_text4 = 'Mississippi'
    sample_text5 = 'aabbccddeeff'
    print(find_repeated_letters(sample_text1))
    print(find_repeated_letters(sample_text2))
    print(find_repeated_letters(sample_text3))
    print(find_repeated_letters(sample_text4))
    print(find_repeated_letters(sample_text5))