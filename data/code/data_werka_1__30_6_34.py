def swap_adjacent_chars(s):
    char_list = list(s)
    for i in range(len(char_list) - 1):
        temp = char_list[i]
        char_list[i] = char_list[i + 1]
        char_list[i + 1] = temp
    return ''.join(char_list)

if __name__ == '__main__':
    sample_input = "abcdef"
    swapped_string = swap_adjacent_chars(sample_input)
    print(swapped_string)