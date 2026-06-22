class StringCleaner:
    WHITESPACE_CHARS = " \t\n\r"

    @staticmethod
    def remove_all_whitespace(input_string: str) -> str:
        translation_table = str.maketrans('', '', StringCleaner.WHITESPACE_CHARS)
        return input_string.translate(translation_table)

if __name__ == '__main__':
    sample1 = "Hello World\nThis has\tmixed spaces."
    sample2 = "Unicode test: \u20AC and some spaces"
    sample3 = "\t\n\r  Multiple\tspaces\tand\tnewlines\n"
    sample4 = "NoWhitespaceHere"
    sample5 = "   \t\n"

    cleaner = StringCleaner()
    print(f"Original 1: '{sample1}'")
    result1 = cleaner.remove_all_whitespace(sample1)
    print(f"Result 1:   '{result1}'\n")

    print(f"Original 2: '{sample2}'")
    result2 = cleaner.remove_all_whitespace(sample2)
    print(f"Result 2:   '{result2}'\n")

    print(f"Original 3: '{sample3}'")
    result3 = cleaner.remove_all_whitespace(sample3)
    print(f"Result 3:   '{result3}'\n")

    print(f"Original 4: '{sample4}'")
    result4 = cleaner.remove_all_whitespace(sample4)
    print(f"Result 4:   '{result4}'\n")

    print(f"Original 5: '{sample5}'")
    result5 = cleaner.remove_all_whitespace(sample5)
    print(f"Result 5:   '{result5}'\n")