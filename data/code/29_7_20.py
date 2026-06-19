def reverse_string(input_string):
    if isinstance(input_string, str):
        return input_string[::-1]
    else:
        raise ValueError("Input must be a string")

if __name__ == '__main__':
    sample_input = "Hello, World!"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)