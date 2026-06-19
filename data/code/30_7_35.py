def reverse_string_by_swapping(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n // 2):
        if s_list[i] != s_list[n - i - 1]:
            s_list[i], s_list[i + 1] = (s_list[i + 1], s_list[i])
            s_list[n - i - 1], s_list[n - i - 2] = (s_list[n - i - 2], s_list[n - i - 1])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string = 'abcdef'
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)