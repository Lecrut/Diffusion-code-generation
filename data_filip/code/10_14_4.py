from collections import deque

def reverse_words(s):
    if not s:
        return ""
    
    words = deque()
    current_word = []
    
    for char in s:
        if char == ' ':
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:
        words.append(''.join(current_word))
    
    words.reverse()
    
    if not words:
        return ""
    
    result = words[0]
    for word in words[1:]:
        result += ' ' + word
    
    return result

if __name__ == "__main__":
    test_cases = [
        "hello world this is a test",
        "  leading and trailing spaces  ",
        "",
        "   ",
        "single",
        "multiple   spaces   between   words"
    ]
    
    for case in test_cases:
        reversed_text = reverse_words(case)
        print(f"Input: '{case}' -> Output: '{reversed_text}'")