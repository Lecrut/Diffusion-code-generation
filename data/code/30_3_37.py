def reverse_adjacent_swaps(s):
    chars = list(s)
    n = len(chars)
    for i in range(0, n - 1, 2):
        chars[i], chars[i + 1] = (chars[i + 1], chars[i])
    return ''.join(chars)
if __name__ == '__main__':
    sample_input = 'abcdef'
    result = reverse_adjacent_swaps(sample_input)
    print(result)