def reverse_string(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

if __name__ == '__main__':
    sample_string = "Hello, Alibaba Cloud!"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)