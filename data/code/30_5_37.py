def swap_adjacent_chars(s):
    if len(s) < 2:
        return s
    chars = list(s)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_adjacent_chars(sample_string)
    print(result)