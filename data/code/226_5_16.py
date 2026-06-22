def repeat_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s * 4

if __name__ == '__main__':
    sample_value = "hello"
    result = repeat_string(sample_value)
    print(result)