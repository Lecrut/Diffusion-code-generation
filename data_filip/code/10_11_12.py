def reverse_words(sentence: str) -> str:
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    test_cases = [
        "  Hello   world  ",
        "  multiple   spaces   between   words  ",
        "NoExtraSpaces",
        "   leading and trailing   ",
        "a   b   c"
    ]
    for case in test_cases:
        print(reverse_words(case))