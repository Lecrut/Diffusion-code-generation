def swap_characters(s):
    char_list = list(s)
    length = len(char_list)
    for i in range(0, length - 1, 2):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'abcdef'
    result = swap_characters(sample_string)
    print(result)