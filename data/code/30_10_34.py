def swap_adjacent_characters(s):
    char_list = list(s)
    swapped_list = [char_list[i + 1] + char_list[i] if i % 2 == 0 else char_list[i] for i in range(len(char_list) - 1)]
    if len(char_list) % 2 != 0:
        swapped_list.append(char_list[-1])
    return ''.join(swapped_list)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    result = swap_adjacent_characters(sample_string)
    print(result)