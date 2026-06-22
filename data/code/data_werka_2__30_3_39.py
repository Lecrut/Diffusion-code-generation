def reverse_adjacent_swaps(s):
    char_list = list(s)
    length = len(char_list)
    for i in range(0, length - 1, 2):
        temp = char_list[i]
        char_list[i] = char_list[i + 1]
        char_list[i + 1] = temp
    return ''.join(char_list)
if __name__ == '__main__':
    sample_input = 'hello world'
    result = reverse_adjacent_swaps(sample_input)
    print(result)