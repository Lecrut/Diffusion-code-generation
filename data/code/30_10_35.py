def swap_adjacent_characters(s):
    return ''.join([s[i:i+2][::-1] for i in range(0, len(s), 2)])

if __name__ == '__main__':
    sample_string = "abcdefg"
    swapped_string = swap_adjacent_characters(sample_string)
    print(swapped_string)