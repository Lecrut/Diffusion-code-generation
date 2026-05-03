def minify_text(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
if __name__ == '__main__':
    sample1 = "  Hello World! \n This is a test. "
    sample2 = "NoWhitespaceHere"
    sample3 = "Multiple\tspaces\nand\rnewlines"
    sample4 = ""
    print(f"Original 1: '{sample1}'")
    print(f"Minified 1: '{minify_text(sample1)}'")
    print("-" * 20)
    print(f"Original 2: '{sample2}'")
    print(f"Minified 2: '{minify_text(sample2)}'")
    print("-" * 20)
    print(f"Original 3: '{sample3}'")
    print(f"Minified 3: '{minify_text(sample3)}'")
    print("-" * 20)
    print(f"Original 4: '{sample4}'")
    print(f"Minified 4: '{minify_text(sample4)}'")