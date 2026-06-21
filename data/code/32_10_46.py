def string_length(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return len(s)

if __name__ == '__main__':
    test_string = "Alibaba Cloud"
    length_of_string = string_length(test_string)
    print(length_of_string)