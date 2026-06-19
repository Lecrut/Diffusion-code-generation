def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    SAMPLE_INPUT = "Alibaba Cloud"
    REVERSED_OUTPUT = reverse_string(SAMPLE_INPUT)
    print(REVERSED_OUTPUT)