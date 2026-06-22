from collections import deque
import re

def reverse_words(text: str) -> str:
    if not text:
        return text
    words = text.split()
    if not words:
        return text
    word_deque = deque(words)
    word_deque.reverse()
    return " ".join(word_deque)

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("  spaces   everywhere  "))
    print(reverse_words(""))
    print(reverse_words("   "))
    print(reverse_words("Single"))