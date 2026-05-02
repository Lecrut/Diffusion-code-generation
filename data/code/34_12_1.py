class StringUtils:
    @staticmethod
    def capitalizeWords(input_string: str) -> str:
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string.")
        words = input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    sample1 = "hello world this is a test"
    sample2 = "this-is-another-example"
    sample3 = "a short sentence"
    sample4 = "  leading and trailing spaces  "
    sample5 = ""
    sample6 = "singleword"
    print(f"Input: '{sample1}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample1)}'")
    print("-" * 20)
    print(f"Input: '{sample2}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample2)}'")
    print("-" * 20)
    print(f"Input: '{sample3}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample3)}'")
    print("-" * 20)
    print(f"Input: '{sample4}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample4)}'")
    print("-" * 20)
    print(f"Input: '{sample5}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample5)}'")
    print("-" * 20)
    print(f"Input: '{sample6}'")
    print(f"Output: '{StringUtils.capitalizeWords(sample6)}'")
    print("-" * 20)