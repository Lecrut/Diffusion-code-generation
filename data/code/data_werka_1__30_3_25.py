def reverse_adjacent_swaps(s):
    s_list = list(s)
    for i in range(0, len(s_list) - 1, 2):
        s_list[i], s_list[i + 1] = (s_list[i + 1], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_input_1 = 'abcdef'
    sample_input_2 = 'a'
    sample_input_3 = 'ab'
    sample_input_4 = 'abcde'
    print(reverse_adjacent_swaps(sample_input_1))
    print(reverse_adjacent_swaps(sample_input_2))
    print(reverse_adjacent_swaps(sample_input_3))
    print(reverse_adjacent_swaps(sample_input_4))