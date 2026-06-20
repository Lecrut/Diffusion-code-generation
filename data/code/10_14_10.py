from collections import deque

def reverse_words(s: str) -> str:
    if not s or not s.strip():
        return ""
    words = s.split()
    word_deque = deque(words)
    reversed_words = []
    while word_deque:
        reversed_words.append(word_deque.pop())
    return " ".join(reversed_words)

if __name__ == "__main__":
    test_cases = [
        "The quick brown fox jumps over the lazy dog",
        "  hello   world  ",
        "",
        "   ",
        "single"
    ]
    for test_input in test_cases:
        result = reverse_words(test_input)
        print(f"Input: '{test_input}' -> Output: '{result}'")