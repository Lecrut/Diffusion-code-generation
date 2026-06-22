def reverse_word(word):
    char_list = list(word)
    length = len(char_list)
    for i in range(length // 2):
        char_list[i], char_list[length - i - 1] = char_list[length - i - 1], char_list[i]
    return ''.join(char_list)

if __name__ == '__main__':
    sample_word = 'world'
    print(reverse_word(sample_word))