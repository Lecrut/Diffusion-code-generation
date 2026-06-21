def reverse_words(s):
    words = s.split()
    if not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a string containing only words.")
    reversed_words = list(reversed(words))
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "The quick brown fox"
    result = reverse_words(test_string)
    print(result)