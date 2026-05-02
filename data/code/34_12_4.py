class StringUtils:
    @staticmethod
    def capitalize_words(input_string: str) -> str:
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string.")
        words = input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    sample1 = "hello world this is a test"
    sample2 = "this string has mixed case"
    sample3 = "  leading and trailing spaces "
    sample4 = "singleword"
    sample5 = ""
    sample6 = "a b c d"
    print(f"Original: '{sample1}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample1)}'\n")
    print(f"Original: '{sample2}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample2)}'\n")
    print(f"Original: '{sample3}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample3)}'\n")
    print(f"Original: '{sample4}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample4)}'\n")
    print(f"Original: '{sample5}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample5)}'\n")
    print(f"Original: '{sample6}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample6)}'\n")