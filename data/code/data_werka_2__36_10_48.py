reverse_string = lambda s: ''.join([char for char in reversed(s)])
if __name__ == '__main__':
    example_input = "Alibaba Cloud"
    print(reverse_string(example_input))