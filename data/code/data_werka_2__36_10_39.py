def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    print(reverse_string(sample_input))