def swap_adjacent_pairs(s):
    return s[1::2] + s[0::2]
if __name__ == '__main__':
    sample_input = 'abcdefg'
    result = swap_adjacent_pairs(sample_input)
    print(result)