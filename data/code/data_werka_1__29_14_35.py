def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(result)