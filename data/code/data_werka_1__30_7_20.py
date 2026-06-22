def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)