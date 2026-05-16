def swap_adjacent_characters(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n - 1):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    test_string1 = "abcdef"
    result1 = swap_adjacent_characters(test_string1)
    print(result1)
    test_string2 = "hello"
    result2 = swap_adjacent_characters(test_string2)
    print(result2)
    test_string3 = "abcde"
    result3 = swap_adjacent_characters(test_string3)
    print(result3)
    test_string4 = "a"
    result4 = swap_adjacent_characters(test_string4)
    print(result4)
    test_string5 = ""
    result5 = swap_adjacent_characters(test_string5)
    print(result5)