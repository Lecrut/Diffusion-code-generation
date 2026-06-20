from collections import deque

def reverse_words(text):
    if not text:
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
    sample_inputs = [
        "Hello World",
        "",
        "   ",
        "One",
        "Two words here",
        "  Leading and trailing  "
    ]
    
    for sample in sample_inputs:
        result = reverse_words(sample)
        print(result)