from collections import deque

def reverse_words(s: str) -> str:
    words = s.split()
    word_queue = deque(words)
    reversed_words = []
    while word_queue:
        reversed_words.append(word_queue.pop())
    return " ".join(reversed_words)

if __name__ == "__main__":
    test_cases = [
        "Hello World",
        "  Python   is awesome  ",
        "",
        "   ",
        "One"
    ]
    for case in test_cases:
        result = reverse_words(case)
        print(f"Input: '{case}' -> Output: '{result}'")