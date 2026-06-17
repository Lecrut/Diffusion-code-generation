import re
def remove_all_whitespace(input_string: str) -> str:
    return re.sub(r'\s+', '', input_string)
if __name__ == '__main__':
    sample1 = "Hello World\nThis has\tmixed whitespace."
    sample2 = "Unicode Test: \u20AC and some spaces\tand newlines\n\r"
    sample3 = "NoWhitespaceHere"
    sample4 = "\t\n\r  Multiple\tspaces\tand\tnewlines"
    sample5 = "   leading and trailing spaces   "
    print(f"Original 1: '{sample1}'")
    print(f"Processed 1: '{remove_all_whitespace(sample1)}'")
    print("-" * 20)
    print(f"Original 2: '{sample2}'")
    print(f"Processed 2: '{remove_all_whitespace(sample2)}'")
    print("-" * 20)
    print(f"Original 3: '{sample3}'")
    print(f"Processed 3: '{remove_all_whitespace(sample3)}'")
    print("-" * 20)
    print(f"Original 4: '{sample4}'")
    print(f"Processed 4: '{remove_all_whitespace(sample4)}'")
    print("-" * 20)
    print(f"Original 5: '{sample5}'")
    print(f"Processed 5: '{remove_all_whitespace(sample5)}'")