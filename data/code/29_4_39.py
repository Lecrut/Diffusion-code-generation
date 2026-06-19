def reverse_string(s):
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "hello"
    print(reverse_string(sample_string))