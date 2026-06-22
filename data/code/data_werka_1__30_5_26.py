def swap_adjacent_chars(s):
    chars = list(s)
    for i in range(len(chars) - 1):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_adjacent_chars(sample_string)
    print(result)