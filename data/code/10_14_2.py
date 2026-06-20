from collections import deque

def reverse_words(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    stack = deque(words)
    reversed_words = []
    while stack:
        reversed_words.append(stack.pop())
    return " ".join(reversed_words)

if __name__ == "__main__":
    test_cases = [
        "The quick brown fox jumps over the lazy dog",
        "  hello   world  ",
        "",
        "   ",
        "a",
        "single word",
        "multiple   spaces   between"
    ]
    for case in test_cases:
        result = reverse_words(case)
        print(f"Input: '{case}' -> Output: '{result}'")