def swap_even_odd_characters(s):
    return ''.join(s[i+1] + s[i] if i % 2 == 0 else s[i] for i in range(len(s) - 1)) + (s[-1] if len(s) % 2 != 0 else '')

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_even_odd_characters(sample_string)
    print(result)