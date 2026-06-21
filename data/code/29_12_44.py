def reverse_word(word):
    if not word:
        return ""
    
    reversed_chars = []
    for i in range(len(word) - 1, -1, -1):
        reversed_chars.append(word[i])
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "python"
    print(reverse_word(sample_word))