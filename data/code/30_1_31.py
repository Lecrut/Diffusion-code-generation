def swap_adjacent_pairs(s):
    if len(s) < 2:
        return s
    swapped = ''
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            swapped += s[i+1] + s[i]
        else:
            swapped += s[i]
    return swapped

if __name__ == '__main__':
    sample_input = "abcdefg"
    print(swap_adjacent_pairs(sample_input))