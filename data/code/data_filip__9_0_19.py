class TextProcessor:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        self._text = text

    def strip_whitespace(self) -> str:
        return self._text.strip()

if __name__ == '__main__':
    test_cases = [
        "  leading and trailing  ",
        "\t\t\n\nmixed whitespace\n\n\t\t",
        "no whitespace here",
        "   ",
        "",
        "\x00\x01\x02content\x02\x01\x00",
    ]

    for case in test_cases:
        processor = TextProcessor(case)
        cleaned = processor.strip_whitespace()
        print(cleaned)

    try:
        invalid_processor = TextProcessor(123)
    except TypeError:
        print("Caught expected TypeError for non-string input")