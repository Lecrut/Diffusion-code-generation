class StringProcessor:
    @staticmethod
    def get_initial_characters(text: str) -> list[str]:
        words = text.split()
        initials = []
        for word in words:
            if word:
                initials.append(word[0])
        return initials
if __name__ == '__main__':
    sample_string_1 = "Hello world this is a test"
    result_1 = StringProcessor.get_initial_characters(sample_string_1)
    print(f"Input: '{sample_string_1}'")
    print(f"Result: {result_1}")
    sample_string_2 = "  leading spaces and multiple words "
    result_2 = StringProcessor.get_initial_characters(sample_string_2)
    print(f"Input: '{sample_string_2}'")
    print(f"Result: {result_2}")
    sample_string_3 = "singleword"
    result_3 = StringProcessor.get_initial_characters(sample_string_3)
    print(f"Input: '{sample_string_3}'")
    print(f"Result: {result_3}")