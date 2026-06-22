def get_first_word(sentence: str) -> str:
    words = sentence.split()
    return words[0] if words else ""

class SentenceProcessor:
    def __init__(self, text: str):
        self.text = text

    def extract_first_word(self) -> str:
        return get_first_word(self.text)

if __name__ == '__main__':
    processor1 = SentenceProcessor("Hello world, this is a test.")
    print(f"First Word: '{processor1.extract_first_word()}'")

    processor2 = SentenceProcessor("  \t\n Another line starts here.")
    print(f"First Word: '{processor2.extract_first_word()}'")

    processor3 = SentenceProcessor("123numbers and symbols")
    print(f"First Word: '{processor3.extract_first_word()}'")

    processor4 = SentenceProcessor("")
    print(f"First Word: '{processor4.extract_first_word()}'")

    processor5 = SentenceProcessor("   ")
    print(f"First Word: '{processor5.extract_first_word()}'")