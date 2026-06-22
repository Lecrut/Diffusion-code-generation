def swap_adjacent_characters(s):
    return ''.join([s[i+1] + s[i] if i % 2 == 0 else s[i] for i in range(len(s) - 1)]) + s[-1] if len(s) % 2 != 0 else ''.join([s[i+1] + s[i] for i in range(0, len(s), 2)])

if __name__ == '__main__':
    sample_string = "abcdefg"
    print(swap_adjacent_characters(sample_string))