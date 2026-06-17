import re
def remove_all_whitespace(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    pattern = r'\s+'
    result = re.sub(pattern, '', input_string)
    return result
if __name__ == '__main__':
    sample1 = "Hello World\nThis has\tmixed whitespace."
    sample2 = "Unicode test: \u20AC and \u00E9"
    sample3 = "\t\n\r  Multiple\tspaces\nand\tnewlines."
    sample4 = "NoWhitespaceHere"
    sample5 = ""
    print(f"Original 1: '{sample1}'")
    print(f"Cleaned 1:  '{remove_all_whitespace(sample1)}'")
    print("-" * 20)
    print(f"Original 2: '{sample2}'")
    print(f"Cleaned 2:  '{remove_all_whitespace(sample2)}'")
    print("-" * 20)
    print(f"Original 3: '{sample3}'")
    print(f"Cleaned 3:  '{remove_all_whitespace(sample3)}'")
    print("-" * 20)
    print(f"Original 4: '{sample4}'")
    print(f"Cleaned 4:  '{remove_all_whitespace(sample4)}'")
    print("-" * 20)
    print(f"Original 5: '{sample5}'")
    print(f"Cleaned 5:  '{remove_all_whitespace(sample5)}'")