def reverse_word(word):
    if not word:
        return ""
    
    reversed_chars = [''] * len(word)
    index = 0
    
    for char in word:
        reversed_chars[len(word) - 1 - index] = char
        index += 1
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "optimization"
    print(reverse_word(sample_word))