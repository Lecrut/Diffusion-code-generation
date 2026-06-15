class TextParser:
    def parse(self, text_data):
        tokens = []
        for char in text_data:
            if char.isalnum():
                tokens.append(char)
        return tokens
if __name__ == '__main__':
    parser = TextParser()
    sample_text = "Hello world! This is a test, how are you doing?"
    cleaned_tokens = parser.parse(sample_text)
    print(cleaned_tokens)