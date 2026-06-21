def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    test_input = "Alibaba Cloud"
    print(reverse_string(test_input))