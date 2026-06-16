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
    print(f"Input: '{sample_string1}'")
    print(f"Result: {result1}")
    sample_string2 = "Python programming example"
    result2 = StringProcessor.get_initial_characters(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Result: {result2}")
    sample_string3 = "singleword"
    result3 = StringProcessor.get_initial_characters(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Result: {result3}")
    sample_string4 = ""
    result4 = StringProcessor.get_initial_characters(sample_string4)
    print(f"Input: '{sample_string4}'")
    print(f"Result: {result4}")