def trim_spaces(value):
    return value.strip()

if __name__ == '__main__':
    sample_input = "  hello world  "
    result = trim_spaces(sample_input)
    print(result)