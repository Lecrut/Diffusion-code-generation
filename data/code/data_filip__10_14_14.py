from collections import deque

def reverse_words(s):
    if not s:
        return ""
    words = s.split()
    if not words:
        return ""
    word_deque = deque(words)
    reversed_words = []
    while word_deque:
        reversed_words.append(word_deque.pop())
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "  spaces  everywhere  ",
        "",
        "   ",
        "single",
        "one two three four"
    ]
    for s in sample_strings:
        result = reverse_words(s)
        print(result)