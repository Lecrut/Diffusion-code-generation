def calculate_length(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    length = 0
    for _ in s:
        length += 1
    return length

if __name__ == '__main__':
    sample_string = "Next-Generation AI"
    print(calculate_length(sample_string))