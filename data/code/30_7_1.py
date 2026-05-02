def swap_adjacent_characters(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n - 1):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    input_string = "abcdefg"
    result = swap_adjacent_characters(input_string)
    print(result)