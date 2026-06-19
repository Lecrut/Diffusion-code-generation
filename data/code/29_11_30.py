def reverse_word(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)

if __name__ == '__main__':
    SAMPLE_WORD_1 = "hello"
    SAMPLE_WORD_2 = "world"
    SAMPLE_WORD_3 = "Python"

    reversed_word_1 = reverse_word(SAMPLE_WORD_1)
    reversed_word_2 = reverse_word(SAMPLE_WORD_2)
    reversed_word_3 = reverse_word(SAMPLE_WORD_3)

    print(f"'{SAMPLE_WORD_1}' reversed is '{reversed_word_1}'")
    print(f"'{SAMPLE_WORD_2}' reversed is '{reversed_word_2}'")
    print(f"'{SAMPLE_WORD_3}' reversed is '{reversed_word_3}'")