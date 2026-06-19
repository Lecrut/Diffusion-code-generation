def swap_adjacent_pairs(s):
    result = []
    for i in range(0, len(s) - 1, 2):
        result.append(s[i+1])
        result.append(s[i])
    if len(s) % 2 != 0:
        result.append(s[-1])
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdefg"
    print(swap_adjacent_pairs(sample_input))