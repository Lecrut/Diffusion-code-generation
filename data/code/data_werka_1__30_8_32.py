def swap_characters(s):
    char_list = list(s)
    n = len(char_list)
    for i in range(0, n - 1, 2):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_input = 'abcdef'
    result = swap_characters(sample_input)
    print(result)