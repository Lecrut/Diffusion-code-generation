def swap_characters(s):
    return ''.join([s[i+1] + s[i] if i + 1 < len(s) else s[i] for i in range(0, len(s), 2)])

if __name__ == '__main__':
    sample_string = 'abcdefg'
    swapped_string = swap_characters(sample_string)
    print(swapped_string)