def reverse_word(word):
    if not word:
        return ""
    reversed_chars = [''] * len(word)
    for i in range(len(word)):
        reversed_chars[len(word) - 1 - i] = word[i]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "python"
    print(reverse_word(sample_word))