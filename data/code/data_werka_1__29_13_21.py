def reverse_word(word):
    reversed_word = ''
    for char in range(len(word) - 1, -1, -1):
        reversed_word += word[char]
    return reversed_word

if __name__ == '__main__':
    sample_word = 'hello'
    print(reverse_word(sample_word))