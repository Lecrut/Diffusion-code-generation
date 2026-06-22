def reverse_word(word):
    if not word:
        return ""
    
    reversed_chars = []
    for char in reversed(word):
        reversed_chars.append(char)
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "hello"
    print(reverse_word(sample_word))