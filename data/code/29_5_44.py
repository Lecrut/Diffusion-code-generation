def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_input = "Alibaba"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)