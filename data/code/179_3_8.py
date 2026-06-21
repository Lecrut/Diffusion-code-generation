def reverse_words(s):
    words = s.split()
    if not all(isinstance(w, str) for w in words):
        raise ValueError("All elements must be strings")
    reversed_words = list(reversed(words))
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string = "The quick brown fox"
    print(reverse_words(test_string))