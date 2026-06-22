def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    for i in range(n // 2):
        j = n - i - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)