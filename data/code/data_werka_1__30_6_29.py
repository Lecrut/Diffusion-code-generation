def swap_adjacent_characters(s):
    CHAR_SWAP_STEP = 2
    char_list = list(s)
    for i in range(0, len(char_list) - 1, CHAR_SWAP_STEP):
        char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    return ''.join(char_list)

if __name__ == '__main__':
    SAMPLE_INPUT = "abcdefg"
    RESULT = swap_adjacent_characters(SAMPLE_INPUT)
    print(RESULT)