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
    test_string1 = "abcdefgh"
    result1 = swap_even_odd(test_string1)
    print(f"Input: {test_string1}, Output: {result1}")
    test_string2 = "abcde"
    result2 = swap_even_odd(test_string2)
    print(f"Input: {test_string2}, Output: {result2}")
    test_string3 = "a"
    result3 = swap_even_odd(test_string3)
    print(f"Input: {test_string3}, Output: {result3}")
    test_string4 = ""
    result4 = swap_even_odd(test_string4)
    print(f"Input: {test_string4}, Output: {result4}")
    test_string5 = "123456"
    result5 = swap_even_odd(test_string5)
    print(f"Input: {test_string5}, Output: {result5}")