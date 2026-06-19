def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            s[j], s[j + 1] = s[j + 1], s[j]
    return ''.join(s)

if __name__ == '__main__':
    original_string = "hello"
    reversed_string = reverse_string_by_swapping(original_string)
    print(reversed_string)