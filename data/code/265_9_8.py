import math

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return n == root * root

def extract_by_ascii_sqrt(phrase):
    result = []
    for char in phrase:
        ascii_val = ord(char)
        if is_perfect_square(ascii_val):
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase1 = "Hello, World!"
    sample_phrase2 = "Python 3.8"
    print(f"'{sample_phrase1}': {extract_by_ascii_sqrt(sample_phrase1)}")
    print(f"'{sample_phrase2}': {extract_by_ascii_sqrt(sample_phrase2)}")