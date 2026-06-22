def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_input = "hello"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)