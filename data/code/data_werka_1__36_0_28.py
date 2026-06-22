def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    SAMPLE_STRING = "hello world"
    REVERSED_STRING = reverse_string(SAMPLE_STRING)
    print(REVERSED_STRING)