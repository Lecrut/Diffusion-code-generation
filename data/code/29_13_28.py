def reverse_word(word):
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

if __name__ == '__main__':
    sample_word = 'example'
    print(reverse_word(sample_word))