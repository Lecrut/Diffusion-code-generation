from collections import deque

def reverse_words(s: str) -> str:
    if not s:
        return s
    words = s.split()
    word_deque = deque(words)
    reversed_words = []
    while word_deque:
        reversed_words.append(word_deque.pop())
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = ""
    sample3 = "   "
    sample4 = "  Hello   World  "
    sample5 = "SingleWord"
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))