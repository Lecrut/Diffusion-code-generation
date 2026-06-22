def remove_all_whitespace(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    translation_table = str.maketrans('', '', ' \t\n\r\x0c\x0b')
    return input_string.translate(translation_table)
if __name__ == '__main__':
    sample1 = 'Hello World\nThis has\tmixed spaces.'
    sample2 = 'Unicode: € and some spaces\tand newlines\n\r'
    sample3 = 'NoWhitespaceHere'
    sample4 = '\t\n  Multiple\tspaces\r\n'
    sample5 = '   \t\n'
    print(f"Original 1: '{sample1}'")
    result1 = remove_all_whitespace(sample1)
    print(f"Result 1:   '{result1}'\n")
    print(f"Original 2: '{sample2}'")
    result2 = remove_all_whitespace(sample2)
    print(f"Result 2:   '{result2}'\n")
    print(f"Original 3: '{sample3}'")
    result3 = remove_all_whitespace(sample3)
    print(f"Result 3:   '{result3}'\n")
    print(f"Original 4: '{sample4}'")
    result4 = remove_all_whitespace(sample4)
    print(f"Result 4:   '{result4}'\n")
    print(f"Original 5: '{sample5}'")
    result5 = remove_all_whitespace(sample5)
    print(f"Result 5:   '{result5}'\n")