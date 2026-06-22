class TextProcessor:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def _split_text(text):
        return text.split()

    @staticmethod
    def _extract_first_letters(words):
        return [word[0] for word in words if word]

    def get_first_letters(self):
        words = self._split_text(self.text)
        first_letters = self._extract_first_letters(words)
        return "".join(first_letters)

if __name__ == '__main__':
    sample_string_1 = "  Hello world, this is a test "
    sample_string_2 = "multiple   spaces\tand\nnewlines"
    sample_string_3 = "singleword"
    sample_string_4 = "   "
    sample_string_5 = ""

    processor_1 = TextProcessor(sample_string_1)
    print(processor_1.get_first_letters())

    processor_2 = TextProcessor(sample_string_2)
    print(processor_2.get_first_letters())

    processor_3 = TextProcessor(sample_string_3)
    print(processor_3.get_first_letters())

    processor_4 = TextProcessor(sample_string_4)
    print(processor_4.get_first_letters())

    processor_5 = TextProcessor(sample_string_5)
    print(processor_5.get_first_letters())