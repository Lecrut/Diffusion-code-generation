def swap_adjacent_characters(s):
    return s[1::2] + s[::2]

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_adjacent_characters(sample_string)
    print(result)