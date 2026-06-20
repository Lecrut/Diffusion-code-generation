from collections import deque

def reverse_words(s: str) -> str:
    if not s or not s.strip():
        return ""
    
    words = deque(s.split())
    
    reversed_words = deque()
    while words:
        reversed_words.append(words.pop())
    
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "   "
    sample3 = ""
    sample4 = "a"
    sample5 = "  hello   world  "
    
    print(reverse_words(sample1))
    print(reverse_words(sample2))
    print(reverse_words(sample3))
    print(reverse_words(sample4))
    print(reverse_words(sample5))