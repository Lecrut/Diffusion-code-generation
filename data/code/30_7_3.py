def swap_adjacent_characters(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n - 1):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_adjacent_characters(sample_string)
    print(result)
    sample_string_2 = "hello"
    result_2 = swap_adjacent_characters(sample_string_2)
    print(result_2)
    sample_string_3 = "abcde"
    result_3 = swap_adjacent_characters(sample_string_3)
    print(result_3)