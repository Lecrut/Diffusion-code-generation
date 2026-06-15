import re
def remove_all_whitespace(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    return re.sub(r'\s+', '', input_string)
if __name__ == '__main__':
    sample1 = "Hello World\nThis has\tmixed whitespace."
    sample2 = "Unicode test: \u20AC and some spaces\tand newlines\n\r"
    sample3 = "NoWhitespaceHere"
    sample4 = "\t\n\r\f\v"
    sample5 = ""
    sample6 = "   \t\n  "
    print(f"Original 1: {repr(sample1)}")
    result1 = remove_all_whitespace(sample1)
    print(f"Result 1: {repr(result1)}\n")
    print(f"Original 2: {repr(sample2)}")
    result2 = remove_all_whitespace(sample2)
    print(f"Result 2: {repr(result2)}\n")
    print(f"Original 3: {repr(sample3)}")
    result3 = remove_all_whitespace(sample3)
    print(f"Result 3: {repr(result3)}\n")
    print(f"Original 4: {repr(sample4)}")
    result4 = remove_all_whitespace(sample4)
    print(f"Result 4: {repr(result4)}\n")
    print(f"Original 5: {repr(sample5)}")
    result5 = remove_all_whitespace(sample5)
    print(f"Result 5: {repr(result5)}\n")
    print(f"Original 6: {repr(sample6)}")
    result6 = remove_all_whitespace(sample6)
    print(f"Result 6: {repr(result6)}\n")