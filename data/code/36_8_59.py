def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "Alibaba Cloud AI"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)