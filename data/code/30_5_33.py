def swap_adjacent_chars(s):
    return ''.join([s[i:i+2][::-1] for i in range(0, len(s), 2)])

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_adjacent_chars(sample_string)
    print(result)