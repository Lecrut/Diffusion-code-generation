def separate_even_odd_ascii(phrase):
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase1 = "Python3.8"
    result1_even, result1_odd = separate_even_odd_ascii(sample_phrase1)
    print(result1_even)
    print(result1_odd)

    sample_phrase2 = "1234567890"
    result2_even, result2_odd = separate_even_odd_ascii(sample_phrase2)
    print(result2_even)
    print(result2_odd)

    sample_phrase3 = "abcdefg"
    result3_even, result3_odd = separate_even_odd_ascii(sample_phrase3)
    print(result3_even)
    print(result3_odd)