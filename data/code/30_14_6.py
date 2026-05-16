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
    sample1 = "abcdefgh"
    sample2 = "hello"
    sample3 = "abcde"
    sample4 = "a"
    sample5 = ""
    print(f"Input: {sample1}, Output: {swap_even_odd(sample1)}")
    print(f"Input: {sample2}, Output: {swap_even_odd(sample2)}")
    print(f"Input: {sample3}, Output: {swap_even_odd(sample3)}")
    print(f"Input: {sample4}, Output: {swap_even_odd(sample4)}")
    print(f"Input: {sample5}, Output: {swap_even_odd(sample5)}")