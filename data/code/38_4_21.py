def find_repeated_letters(sentence):
    letter_counts = {}
    for char in sentence:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1
    repeated = [char for char, count in letter_counts.items() if count > 1]
    return sorted(repeated)

if __name__ == '__main__':
    test_sentences = [
        "Hello World",
        "Python Programming",
        "abcdef",
        "aAbBcC"
    ]
    for sentence in test_sentences:
        result = find_repeated_letters(sentence)
        print(result)