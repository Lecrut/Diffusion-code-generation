import math

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return n == root * root

def extract_by_ascii_value(s):
    result = ''
    for char in s:
        if is_perfect_square(ord(char)):
            result += char
    return result
if __name__ == '__main__':
    test_string1 = 'a2b3c4d5e'
    print(extract_by_ascii_value(test_string1))