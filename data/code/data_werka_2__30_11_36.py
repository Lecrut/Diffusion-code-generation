def swap_even_odd_indices(s):
    if len(s) % 2 != 0:
        raise ValueError('Input string length must be even')
    char_list = list(s)
    for i in range(0, len(char_list), 2):
        char_list[i], char_list[i + 1] = (char_list[i + 1], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_input = 'abcdef'
    result = swap_even_odd_indices(sample_input)
    print(result)