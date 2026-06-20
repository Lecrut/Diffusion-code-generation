from collections import deque

def reverse_words(s):
    if not s:
        return ""
    words = deque(s.split())
    reversed_words = deque()
    while words:
        reversed_words.append(words.pop())
    return " ".join(reversed_words)

if __name__ == "__main__":
    print(reverse_words("hello world"))
    print(reverse_words("  "))
    print(reverse_words(""))
    print(reverse_words("single"))
    print(reverse_words("  leading and trailing  "))