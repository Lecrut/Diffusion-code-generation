def swap_even_odd_characters(s):
    if len(s) < 2:
        return s
    char_list = list(s)
    for i in range(0, len(char_list) - 1, 2):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    swapped_string = swap_even_odd_characters(sample_string)
    print(swapped_string)