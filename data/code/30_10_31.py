def swap_adjacent_characters(s):
    chars = list(s)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = (chars[i + 1], chars[i])
    return ''.join(chars)
if __name__ == '__main__':
    sample_string = 'abcdef'
    swapped_string = swap_adjacent_characters(sample_string)
    print(swapped_string)