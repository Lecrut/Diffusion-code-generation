def strip_whitespace(input_string):
    return input_string.strip()

if __name__ == '__main__':
    samples = ["  hello world  ", "\t\n  test  \r\n", "no_spaces"]
    results = [strip_whitespace(s) for s in samples]
    print(results)