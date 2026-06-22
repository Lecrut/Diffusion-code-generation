def reverse_sentence_in_place(sentence):
    def is_valid_input(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        if len(s) == 0:
            return False
        return True

    def reverse_word(word):
        return word[::-1]

    if not is_valid_input(sentence):
        return ""

    words = sentence.split()
    reversed_words = [reverse_word(word) for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_cases = [
        "Hello world this is a test",
        "Python is fun and powerful",
        "Reverse this sentence",
        "A quick brown fox",
        "Keep it simple"
    ]
    for sentence in test_cases:
        print(reverse_sentence_in_place(sentence))