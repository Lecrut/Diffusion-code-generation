class StringProcessor:
    def __init__(self):
        self._initials = []

    def find_first_word_initial(self, text: str) -> None:
        if not text.strip():
            return
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                self._initials.append(char)
                break

    def get_initials(self) -> list:
        return self._initials

if __name__ == '__main__':
    processor = StringProcessor()
    sample_strings = [
        "Hello world, this is a test.",
        "   \t\nStart here.",
        "123numbers",
        "!@#$%^&*()",
        "ValidWord"
    ]
    
    for sample in sample_strings:
        processor.find_first_word_initial(sample)
    
    print(processor.get_initials())