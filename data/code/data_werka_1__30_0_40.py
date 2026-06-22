def swap_characters(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(0, n - 1, 2):
        s_list[i], s_list[i + 1] = (s_list[i + 1], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_input = 'abcdefg'
    result = swap_characters(sample_input)
    print(result)