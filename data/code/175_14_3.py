class StringManipulator:
    def tokenize_string(self, text: str) -> list[str]:
        return [word for word in text.split() if word]
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = "  Hello world! This is a test, with spaces. "
    tokens = manipulator.tokenize_string(sample_string)
    print(tokens)