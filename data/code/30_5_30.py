def swap_adjacent_chars(s):
    return ''.join([s[i+1] + s[i] if i % 2 == 0 else s[i] for i in range(len(s) - 1)]) + s[-1] if len(s) > 1 else s

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_adjacent_chars(sample_string)
    print(result)