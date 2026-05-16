def swap_even_odd(s):
    n = len(s)
    if n == 0:
        return ""
    chars = list(s)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i+1] = chars[i+1], chars[i]
    return "".join(chars)
if __name__ == '__main__':
    test_string_1 = "abcdefgh"
    result_1 = swap_even_odd(test_string_1)
    print(f"Input: {test_string_1}")
    print(f"Output: {result_1}")
    test_string_2 = "hello"
    result_2 = swap_even_odd(test_string_2)
    print(f"Input: {test_string_2}")
    print(f"Output: {result_2}")
    test_string_3 = "abcde"
    result_3 = swap_even_odd(test_string_3)
    print(f"Input: {test_string_3}")
    print(f"Output: {result_3}")
    test_string_4 = "a"
    result_4 = swap_even_odd(test_string_4)
    print(f"Input: {test_string_4}")
    print(f"Output: {result_4}")
    test_string_5 = ""
    result_5 = swap_even_odd(test_string_5)
    print(f"Input: {test_string_5}")
    print(f"Output: {result_5}")