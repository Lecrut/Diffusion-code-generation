class StringCapitalizer:
    def capitalize_words(self, text):
        words = text.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string_1 = "hello world this is a test"
    sample_string_2 = "the quick brown fox jumps over the lazy dog"
    sample_string_3 = "a short sentence"
    sample_string_4 = "already Capitalized"
    result_1 = capitalizer.capitalize_words(sample_string_1)
    result_2 = capitalizer.capitalize_words(sample_string_2)
    result_3 = capitalizer.capitalize_words(sample_string_3)
    result_4 = capitalizer.capitalize_words(sample_string_4)
    print(f"Original: '{sample_string_1}'")
    print(f"Capitalized: '{result_1}'")
    print("-" * 20)
    print(f"Original: '{sample_string_2}'")
    print(f"Capitalized: '{result_2}'")
    print("-" * 20)
    print(f"Original: '{sample_string_3}'")
    print(f"Capitalized: '{result_3}'")
    print("-" * 20)
    print(f"Original: '{sample_string_4}'")
    print(f"Capitalized: '{result_4}'")