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
    sample4 = "   leading and trailing spaces   "
    sample5 = ""
    sample6 = "singleword"
    print(f"Input: '{sample1}'")
    print(f"Output: '{StringUtils.capitalize_words(sample1)}'\n")
    print(f"Input: '{sample2}'")
    print(f"Output: '{StringUtils.capitalize_words(sample2)}'\n")
    print(f"Input: '{sample3}'")
    print(f"Output: '{StringUtils.capitalize_words(sample3)}'\n")
    print(f"Input: '{sample4}'")
    print(f"Output: '{StringUtils.capitalize_words(sample4)}'\n")
    print(f"Input: '{sample5}'")
    print(f"Output: '{StringUtils.capitalize_words(sample5)}'\n")
    print(f"Input: '{sample6}'")
    print(f"Output: '{StringUtils.capitalize_words(sample6)}'\n")