def swap_even_odd_characters(s):
    return ''.join([s[i+1] + s[i] if i % 2 == 0 and i + 1 < len(s) else s[i] for i in range(len(s))])

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_even_odd_characters(sample_string)
    print(result)