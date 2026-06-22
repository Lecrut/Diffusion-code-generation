def reverse_word(word):
    if not word:
        return ""
    
    reversed_chars = [None] * len(word)
    for i, char in enumerate(word):
        reversed_chars[len(word) - 1 - i] = char
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "example"
    print(reverse_word(sample_word))