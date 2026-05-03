def swap_adjacent(s):
    s_list = list(s)
    for i in range(len(s_list) - 1):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    test_string = "abcde"
    result = swap_adjacent(test_string)
    print(result)