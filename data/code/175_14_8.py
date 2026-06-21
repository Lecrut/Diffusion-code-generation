class StringManipulator:
    def tokenize_string(self, text: str) -> list[str]:
        words = []
        current_word = ""
        for char in text:
            if char == " " and current_word:
                words.append(current_word)
                current_word = ""
            elif char != " ":
                current_word += char
        if current_word:
            words.append(current_word)
        return words

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string1 = "  Hello world! This is a test with multiple   spaces. "
    tokens1 = manipulator.tokenize_string(sample_string1)
    print(tokens1)

    sample_string2 = "  Hello world! This is a test string with extra spaces. "
    tokens2 = manipulator.tokenize_string(sample_string2)
    print(tokens2)

    sample_string3 = "  Hello world!   this is a test. "
    tokens3 = manipulator.tokenize_string(sample_string3)
    print(tokens3)

    sample_string4 = "  Hello world! This is a test, with spaces. "
    tokens4 = manipulator.tokenize_string(sample_string4)
    print(tokens4)