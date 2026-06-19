def reverse_adjacent_swaps(s):
    s_list = list(s)
    for i in range(0, len(s) - 1, 2):
        s_list[i], s_list[i + 1] = (s_list[i + 1], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    result = reverse_adjacent_swaps(sample_string)
    print(result)