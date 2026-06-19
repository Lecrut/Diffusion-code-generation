def reverse_adjacent_swaps(s):
    result = list(s)
    n = len(result)
    for i in range(0, n - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdef"
    print(reverse_adjacent_swaps(sample_input))