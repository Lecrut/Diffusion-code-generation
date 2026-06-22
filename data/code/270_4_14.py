def remove_all_whitespace(input_string: str) -> str:
    return input_string.translate(str.maketrans('', '', ' \t\n\r'))

if __name__ == '__main__':
    sample1 = "Hello World\nThis has\tmixed spaces."
    result1 = remove_all_whitespace(sample1)
    print(f"Result 1:   '{result1}'\n")

    sample2 = "Unicode test: \u20AC and some spaces"
    result2 = remove_all_whitespace(sample2)
    print(f"Result 2:   '{result2}'\n")