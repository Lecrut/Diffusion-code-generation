class StringUtils:
    @staticmethod
    def capitalize_words(input_string: str) -> str:
        if not input_string:
            return ""
        words = input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    sample1 = "hello world this is a test"
    sample2 = "another example string"
    sample3 = "a short sentence"
    sample4 = ""
    sample5 = "tHIS iS a MiXeD cAsE"
    print(f"Original: '{sample1}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample1)}'")
    print("-" * 20)
    print(f"Original: '{sample2}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample2)}'")
    print("-" * 20)
    print(f"Original: '{sample3}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample3)}'")
    print("-" * 20)
    print(f"Original: '{sample4}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample4)}'")
    print("-" * 20)
    print(f"Original: '{sample5}'")
    print(f"Capitalized: '{StringUtils.capitalize_words(sample5)}'")