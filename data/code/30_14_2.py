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
    sample2 = "12345678"
    sample3 = "abcde"
    sample4 = "a"
    sample5 = ""
    print(swap_even_odd(sample1))
    print(swap_even_odd(sample2))
    print(swap_even_odd(sample3))
    print(swap_even_odd(sample4))
    print(swap_even_odd(sample5))