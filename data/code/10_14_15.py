from collections import deque
import re

def reverse_words(text: str) -> str:
    if not text or not text.strip():
        return ""
    words = re.findall(r'\S+', text)
    word_deque = deque(words)
    reversed_words = []
    while word_deque:
        reversed_words.append(word_deque.pop())
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_string_1 = "The quick brown fox"
    test_string_2 = "  hello   world  "
    test_string_3 = ""
    test_string_4 = "   "
    result_1 = reverse_words(test_string_1)
    result_2 = reverse_words(test_string_2)
    result_3 = reverse_words(test_string_3)
    result_4 = reverse_words(test_string_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)