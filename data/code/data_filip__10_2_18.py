def reverse_words(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    test_cases = [
        "Hello   world",
        "  multiple   spaces   between   words  ",
        "SingleWord",
        "   ",
        ""
    ]
    for case in test_cases:
        result = reverse_words(case)
        print(repr(result))