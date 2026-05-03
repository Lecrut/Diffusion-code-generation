def swap_even_odd(s):
    n = len(s)
    result = list(s)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return "".join(result)
if __name__ == '__main__':
    sample_string_1 = "abcdefgh"
    sample_string_2 = "hello"
    sample_string_3 = "abcde"
    sample_string_4 = "123456"
    print(f"Input: {sample_string_1}, Output: {swap_even_odd(sample_string_1)}")
    print(f"Input: {sample_string_2}, Output: {swap_even_odd(sample_string_2)}")
    print(f"Input: {sample_string_3}, Output: {swap_even_odd(sample_string_3)}")
    print(f"Input: {sample_string_4}, Output: {swap_even_odd(sample_string_4)}")