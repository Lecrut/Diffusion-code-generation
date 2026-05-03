class StringCapitalizer:
    def capitalize_words(self, input_string):
        words = input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string_1 = "hello world this is a test"
    sample_string_2 = "this is another example string"
    sample_string_3 = "a short sentence"
    sample_string_4 = "already Capitalized"
    result_1 = capitalizer.capitalize_words(sample_string_1)
    result_2 = capitalizer.capitalize_words(sample_string_2)
    result_3 = capitalizer.capitalize_words(sample_string_3)
    result_4 = capitalizer.capitalize_words(sample_string_4)
    print(f"Input: '{sample_string_1}'")
    print(f"Output: '{result_1}'")
    print("-" * 20)
    print(f"Input: '{sample_string_2}'")
    print(f"Output: '{result_2}'")
    print("-" * 20)
    print(f"Input: '{sample_string_3}'")
    print(f"Output: '{result_3}'")
    print("-" * 20)
    print(f"Input: '{sample_string_4}'")
    print(f"Output: '{result_4}'")