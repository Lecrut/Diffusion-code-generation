def remove_all_whitespace(input_string: str) -> str:
    translator = str.maketrans('', '', ' \t\n\r')
    return input_string.translate(translator)

if __name__ == '__main__':
    sample1 = "Hello World\tThis has mixed spaces.\n"
    sample2 = "Unicode test:\u20AC and some\tspaces\nand newlines."
    
    print(f"Original 1: '{sample1}'")
    result1 = remove_all_whitespace(sample1)
    print(f"Result 1:   '{result1}'\n")
    
    print(f"Original 2: '{sample2}'")
    result2 = remove_all_whitespace(sample2)
    print(f"Result 2:   '{result2}'\n")