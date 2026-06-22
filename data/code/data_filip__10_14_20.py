from collections import deque

def reverse_words(s):
    if not s or not s.strip():
        return ''
    words = s.split()
    if not words:
        return ''
    word_deque = deque(words)
    reversed_words = []
    while word_deque:
        reversed_words.append(word_deque.pop())
    return ' '.join(reversed_words)
if __name__ == '__main__':
    test_cases = ['Hello World', '  Hello   World  ', 'Python is great', '', '   ', 'SingleWord', 'One Two Three Four Five', '  Leading and trailing spaces  ', 'Multiple   spaces   between   words']
    for test in test_cases:
        result = reverse_words(test)
        print(f"Input: '{test}' -> Output: '{result}'")