def reverse_string_generator(input_string):
    length = len(input_string)
    for i in range(length - 1, -1, -1):
        yield input_string[i]

if __name__ == '__main__':
    sample_string = "hello world"
    for char in reverse_string_generator(sample_string):
        print(char, end='')