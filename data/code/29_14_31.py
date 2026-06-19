def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)