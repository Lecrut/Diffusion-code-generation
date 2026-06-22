def reverse_string_generator(s):
    length = len(s)
    for i in range(length - 1, -1, -1):
        yield s[i]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_chars = reverse_string_generator(sample_string)
    print(''.join(reversed_chars))