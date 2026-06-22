def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Multiple   spaces  here  ",
        "SingleWord",
        "   ",
        "One Two Three",
        "Python  is   great"
    ]
    for test in test_cases:
        print(reverse_words(test))