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
    sample2 = "this_is_another_example"
    sample3 = "a short sentence"
    sample4 = ""
    sample5 = "   leading and trailing spaces   "
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