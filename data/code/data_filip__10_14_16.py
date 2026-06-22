from collections import deque

def reverse_words(s: str) -> str:
    words = s.split()
    dq = deque(words)
    reversed_words = []
    while dq:
        reversed_words.append(dq.pop())
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Hello   World  ",
        "",
        "   ",
        "SingleWord",
        "a b c d e",
        "  spaces   everywhere  ",
        "Python is great",
        "Reverse me",
        "1 2 3 4 5"
    ]
    for test in test_cases:
        result = reverse_words(test)
        print(result)