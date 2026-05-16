def swap_even_odd(s):
    n = len(s)
    if n <= 1:
        return s
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    test_string_1 = "abcdef"
    print(f"Input: {test_string_1}, Output: {swap_even_odd(test_string_1)}")
    test_string_2 = "abcde"
    print(f"Input: {test_string_2}, Output: {swap_even_odd(test_string_2)}")
    test_string_3 = "abcde"
    print(f"Input: {test_string_3}, Output: {swap_even_odd(test_string_3)}")
    test_string_4 = "abcd"
    print(f"Input: {test_string_4}, Output: {swap_even_odd(test_string_4)}")
    test_string_5 = "a"
    print(f"Input: {test_string_5}, Output: {swap_even_odd(test_string_5)}")
    test_string_6 = ""
    print(f"Input: {test_string_6}, Output: {swap_even_odd(test_string_6)}")
    test_string_7 = "abcde"
    print(f"Input: {test_string_7}, Output: {swap_even_odd(test_string_7)}")