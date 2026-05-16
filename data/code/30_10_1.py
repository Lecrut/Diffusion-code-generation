def swap_characters(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    s_list = list(s)
    for i in range(0, n - 1, 2):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    test_string_1 = "abcdef"
    result_1 = swap_characters(test_string_1)
    print(f"Input: {test_string_1}, Output: {result_1}")
    test_string_2 = "hello"
    result_2 = swap_characters(test_string_2)
    print(f"Input: {test_string_2}, Output: {result_2}")
    test_string_3 = "abcd"
    result_3 = swap_characters(test_string_3)
    print(f"Input: {test_string_3}, Output: {result_3}")
    test_string_4 = "a"
    result_4 = swap_characters(test_string_4)
    print(f"Input: {test_string_4}, Output: {result_4}")
    test_string_5 = ""
    result_5 = swap_characters(test_string_5)
    print(f"Input: {test_string_5}, Output: {result_5}")