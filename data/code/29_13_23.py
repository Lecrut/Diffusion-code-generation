def reverse_word(word):
    reversed_chars = []
    for char in word:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "example"
    print(reverse_word(sample_word))