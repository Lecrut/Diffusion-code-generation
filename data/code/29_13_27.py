def reverse_word(word):
    reversed_word = []
    for char in word:
        reversed_word.insert(0, char)
    return ''.join(reversed_word)

if __name__ == '__main__':
    sample_word = "hello"
    print(reverse_word(sample_word))