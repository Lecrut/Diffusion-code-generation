def is_perfect_square(n):
    root = int(n ** 0.5)
    return n == root * root

def extract_special_chars(s):
    result = []
    for char in s:
        if is_perfect_square(ord(char)):
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string1 = "a(b(c)d)e"
    sample_string2 = "(a(b)c)(d)"
    print(f"'{sample_string1}': {extract_special_chars(sample_string1)}")
    print(f"'{sample_string2}': {extract_special_chars(sample_string2)}")