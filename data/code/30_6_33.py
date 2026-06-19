def swap_adjacent_characters(s):
    CHAR_LIST = list(s)
    LENGTH = len(CHAR_LIST) - 1
    for i in range(LENGTH):
        CHAR_LIST[i], CHAR_LIST[i + 1] = CHAR_LIST[i + 1], CHAR_LIST[i]
    return ''.join(CHAR_LIST)

if __name__ == '__main__':
    SAMPLE_STRING = 'abcdefg'
    RESULT = swap_adjacent_characters(SAMPLE_STRING)
    print(RESULT)