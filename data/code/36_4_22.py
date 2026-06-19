def reverse_string_generator(s):
    index = len(s) - 1
    while index >= 0:
        yield s[index]
        index -= 1

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_chars = reverse_string_generator(sample_string)
    for char in reversed_chars:
        print(char, end='')