def reverse_words(s):
    if not isinstance(s, str) or len(s.split()) < 2:
        return "Invalid input: Must be a string with at least two words"
    words = s.split()
    reversed_words = list(reversed(words))
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "The quick brown fox"
    result = reverse_words(test_string)
    print(result)