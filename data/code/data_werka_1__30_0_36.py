def swap_characters(s):
    s = list(s)
    for i in range(0, len(s) - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_characters(sample_string)
    print(result)