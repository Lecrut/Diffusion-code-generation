def reverse_string(s):
    n = len(s)
    reversed_chars = [''] * n
    for i in range(n):
        reversed_chars[n - 1 - i] = s[i]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(reverse_string(sample_string))