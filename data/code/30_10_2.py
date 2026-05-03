def swap_characters(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    s_list = list(s)
    for i in range(0, n - 1, 2):
        s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)
if __name__ == '__main__':
    test_string1 = "abcdef"
    result1 = swap_characters(test_string1)
    print(f"Input: {test_string1}, Output: {result1}")
    test_string2 = "hello"
    result2 = swap_characters(test_string2)
    print(f"Input: {test_string2}, Output: {result2}")
    test_string3 = "abcd"
    result3 = swap_characters(test_string3)
    print(f"Input: {test_string3}, Output: {result3}")
    test_string4 = "a"
    result4 = swap_characters(test_string4)
    print(f"Input: {test_string4}, Output: {result4}")
    test_string5 = ""
    result5 = swap_characters(test_string5)
    print(f"Input: '{test_string5}', Output: '{result5}'")