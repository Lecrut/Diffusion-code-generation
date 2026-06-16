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
    sample_string1 = "Hello world this is a test"
    result1 = StringProcessor.get_initial_characters(sample_string1)
    print(result1)
    sample_string2 = "  leading spaces and multiple words "
    result2 = StringProcessor.get_initial_characters(sample_string2)
    print(result2)
    sample_string3 = "singleword"
    result3 = StringProcessor.get_initial_characters(sample_string3)
    print(result3)