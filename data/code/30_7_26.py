def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] != s[j + 1]:
                s[j], s[j + 1] = (s[j + 1], s[j])
    return ''.join(s)
if __name__ == '__main__':
    sample_string = 'hello'
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)