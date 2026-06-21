def split_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s.split()

if __name__ == '__main__':
    test_string = "split this string by spaces"
    result = split_string(test_string)
    print(result)