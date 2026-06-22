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

if __name__ == '__main__':
    sample1 = "Hello World"
    print(reverse_words(sample1))
    
    sample2 = ""
    print(reverse_words(sample2))
    
    sample3 = "   "
    print(reverse_words(sample3))
    
    sample4 = "Single"
    print(reverse_words(sample4))
    
    sample5 = "a b c d e"
    print(reverse_words(sample5))