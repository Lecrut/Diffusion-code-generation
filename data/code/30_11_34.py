def swap_characters(s):
    if len(s) < 2:
        return s
    char_list = list(s)
    for i in range(0, len(char_list) - 1, 2):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_input = 'abcdefg'
    result = swap_characters(sample_input)
    print(result)