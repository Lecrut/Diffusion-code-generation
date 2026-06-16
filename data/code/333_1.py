class StringProcessor:
    def extract_first_letters(self, text: str) -> str:
        result = []
        for word in text.split():
            if word:
                result.append(word[0])
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "This is a sample string for testing optimization"
    output = processor.extract_first_letters(sample_string)
    print(output)