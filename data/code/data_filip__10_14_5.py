from collections import deque

def reverse_words(s):
    words = []
    current_word = []
    in_word = False
    
    for char in s:
        if char == ' ':
            if in_word:
                words.append(''.join(current_word))
                current_word = []
                in_word = False
        else:
            current_word.append(char)
            in_word = True
    
    if current_word:
        words.append(''.join(current_word))
    
    if not words:
        return ""
    
    word_queue = deque(words)
    reversed_words = []
    
    while word_queue:
        reversed_words.append(word_queue.pop())
    
    return " ".join(reversed_words)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Leading and trailing spaces  ",
        "   ",
        "",
        "One",
        "A B C D E"
    ]
    
    for case in test_cases:
        result = reverse_words(case)
        print(f"Input: '{case}' -> Output: '{result}'")