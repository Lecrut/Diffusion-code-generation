def swap_adjacent_characters(s):
    char_list = list(s)
    swapped_list = [char_list[i + 1] if i % 2 == 0 else char_list[i - 1] for i in range(len(char_list))]
    return ''.join(swapped_list)
if __name__ == '__main__':
    sample_string = 'abcdef'
    result = swap_adjacent_characters(sample_string)
    print(result)