from collections import deque

def reverse_words(s):
    words = s.split()
    word_deque = deque(words)
    reversed_deque = deque(reversed(word_deque))
    reversed_string = ' '.join(reversed_deque)
    return reversed_string
if __name__ == '__main__':
    test_cases = ['Hello World', 'Python is awesome', '  Leading and trailing spaces  ', '', '   ', 'OneWord', 'Multiple   spaces   between words']
    for test in test_cases:
        result = reverse_words(test)
        print(f"Input: '{test}' -> Output: '{result}'")