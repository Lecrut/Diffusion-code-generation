reverse_string = lambda s: ''.join([s[i] for i in range(len(s)-1, -1, -1)])
if __name__ == '__main__':
    example_input = "Alibaba Cloud"
    print(reverse_string(example_input))