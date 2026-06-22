def extract_perfect_square_chars(s):
    result = []
    for char in s:
        ascii_val = ord(char)
        if int(ascii_val**0.5)**2 == ascii_val:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    test_string1 = "a(b(c)d)e"
    print(extract_perfect_square_chars(test_string1))