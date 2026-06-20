from collections import deque

def reverse_words(text: str) -> str:
    if not text:
        return ""
    
    words = text.split()
    if not words:
        return ""
    
    word_deque = deque(words)
    word_deque.reverse()
    
    return " ".join(word_deque)

if __name__ == '__main__':
    samples = [
        "Hello World",
        "  spaces   around  ",
        "",
        "singleword",
        "A B C D"
    ]
    
    for sample in samples:
        result = reverse_words(sample)
        print(f"Input: '{sample}' => Output: '{result}'")