from collections import deque

def reverse_words(text):
    if not text or text.isspace():
        return ""
    
    words = text.split()
    if not words:
        return ""
    
    word_deque = deque(words)
    reversed_words = []
    
    while word_deque:
        reversed_words.append(word_deque.pop())
        
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_input = "Hello World from Python"
    result = reverse_words(sample_input)
    print(result)