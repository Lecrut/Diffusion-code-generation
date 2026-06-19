def reverse_string_generator(s):
    for char in reversed(s):
        yield char

if __name__ == '__main__':
    sample_string = "Hello, World!"
    for char in reverse_string_generator(sample_string):
        print(char, end='')