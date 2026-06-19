def swap_characters(s):
    char_list = list(s)
    for i in range(len(char_list) - 1):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'hello'
    result = swap_characters(sample_string)
    print(result)