def reverse_string(s):
    if isinstance(s, str):
        return s[::-1]
    else:
        raise TypeError("Input must be a string")

if __name__ == '__main__':
    sample_input = "Hello, World!"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)