def reverse_string(input_string):
    reversed_chars = []
    for char in input_string:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)