def split_string(input_str):
    return [word for word in input_str.strip().split() if word]

if __name__ == '__main__':
    sample = "   This is  a test string with   multiple spaces. "
    print(split_string(sample))