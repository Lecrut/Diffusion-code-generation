def is_perfect_square(n):
    return int(n**0.5)**2 == n

def extract_chars_by_ascii_value(s):
    return ''.join(char for char in s if is_perfect_square(ord(char)))

if __name__ == '__main__':
    test_string1 = "a(b(c)d)e"
    test_string2 = "(a(b)c)(d)"
    test_string3 = "((x))y"
    test_string4 = "abc"
    test_string5 = "()(())"

    print(extract_chars_by_ascii_value(test_string1))
    print(extract_chars_by_ascii_value(test_string2))
    print(extract_chars_by_ascii_value(test_string3))
    print(extract_chars_by_ascii_value(test_string4))
    print(extract_chars_by_ascii_value(test_string5))