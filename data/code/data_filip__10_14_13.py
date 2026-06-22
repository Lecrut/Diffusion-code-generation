import collections

def reverse_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = text.split()
    
    if not words:
        return ""
    
    deque = collections.deque(words)
    
    result_parts = []
    while deque:
        result_parts.append(deque.popleft())
    
    return " ".join(reversed(result_parts))

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("   spaced   out   "))
    print(reverse_words(""))
    print(reverse_words("single"))
    print(reverse_words("a"))