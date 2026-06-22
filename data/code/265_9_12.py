import math

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return n == root * root

def extract_characters_by_ascii(s):
    result = []
    for char in s:
        if is_perfect_square(ord(char)):
            result.append(char)
    return ''.join(result)
if __name__ == '__main__':
    sample_string1 = 'aBcD'
    sample_string2 = 'helloWorld'
    sample_string3 = 'Python3.8'
    print(extract_characters_by_ascii(sample_string1))
    print(extract_characters_by_ascii(sample_string2))
    print(extract_characters_by_ascii(sample_string3))