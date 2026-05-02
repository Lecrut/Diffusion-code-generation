def minify_text(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
if __name__ == '__main__':
    sample1 = "  Hello World! \nThis is a test. "
    sample2 = "NoWhitespaceHere"
    sample3 = "Tabs\tand\tnewlines\n\r"
    sample4 = "   leading and trailing spaces   "
    sample5 = ""
    print(f"Original: '{sample1}'")
    print(f"Minified: '{minify_text(sample1)}'")
    print("-" * 20)
    print(f"Original: '{sample2}'")
    print(f"Minified: '{minify_text(sample2)}'")
    print("-" * 20)
    print(f"Original: '{sample3}'")
    print(f"Minified: '{minify_text(sample3)}'")
    print("-" * 20)
    print(f"Original: '{sample4}'")
    print(f"Minified: '{minify_text(sample4)}'")
    print("-" * 20)
    print(f"Original: '{sample5}'")
    print(f"Minified: '{minify_text(sample5)}'")
    print("-" * 20)