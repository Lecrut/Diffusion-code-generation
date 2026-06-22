def swap_adjacent_chars(s):
    return ''.join([s[i+1] + s[i] if i % 2 == 0 and i < len(s) - 1 else s[i] for i in range(len(s))])

if __name__ == '__main__':
    sample = "abcdef"
    result = swap_adjacent_chars(sample)
    print(result)