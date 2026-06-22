def swap_adjacent_pairs(s):
    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            result.append(s[i+1])
            result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdefg"
    print(swap_adjacent_pairs(sample_input))